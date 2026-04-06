# Databricks notebook source
from databricks.sdk import WorkspaceClient
from requests.auth import HTTPBasicAuth

w = WorkspaceClient()

client_id = "testing"
client_secret = "testing"
account_id = "testing"

w.secrets.create_scope(scope="admin3")
w.secrets.put_secret(scope="admin3", key="client_id", string_value=client_id)
w.secrets.put_secret(scope="admin3", key="client_secret", string_value=client_secret)
w.secrets.put_secret(scope="admin3", key="account_id", string_value=account_id)


# COMMAND ----------
import base64
import urllib

import requests
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

# Admin credentials from secret scope (SDK returns base64-encoded values)
admin_client_id = base64.b64decode(
    w.secrets.get_secret("admin3", "client_id").value,
).decode("utf-8")
admin_client_secret = base64.b64decode(
    w.secrets.get_secret("admin", "client_secret").value,
).decode("utf-8")
account_id = base64.b64decode(
    w.secrets.get_secret("admin3", "account_id").value,
).decode("utf-8")

account_host = "https://accounts.azuredatabricks.net"

# Get account-level token
resp = requests.post(
    f"{account_host}/oidc/accounts/{account_id}/v1/token",
    auth=HTTPBasicAuth(admin_client_id, admin_client_secret),
    data={"grant_type": "client_credentials", "scope": "all-apis"},
)
print(f"Status: {resp.status_code}")
print(f"Response: {resp.text[:500]}")
resp.raise_for_status()
token = resp.json()["access_token"]

# Step 1: Create service principal + OAuth secret
sp = w.service_principals.create(display_name="lakebase-sp-arxiv")
secret_resp = requests.post(
    f"{account_host}/api/2.0/accounts/{account_id}/servicePrincipals/{sp.id}/credentials/secrets",
    headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
)
print(f"SPN secret Status: {secret_resp.status_code}")
print(f"SPN secret Response: {secret_resp.text[:500]}")
secret_resp.raise_for_status()
client_id = sp.application_id
client_secret = secret_resp.json()["secret"]

import contextlib

# COMMAND ----------
# Step 2: Store credentials in a secret scope
scope_name = "arxiv-agent-scope"
with contextlib.suppress(Exception):
    w.secrets.create_scope(scope=scope_name)
w.secrets.put_secret(scope=scope_name, key="client_id", string_value=client_id)
w.secrets.put_secret(scope=scope_name, key="client_secret", string_value=client_secret)

# COMMAND ----------
# Step 3: Add SPN role to project
import psycopg
from databricks.sdk.service.postgres import (
    PostgresAPI,
    Role,
    RoleAuthMethod,
    RoleIdentityType,
    RoleRoleSpec,
)

project_id = "arxiv-agent-lakebase"
w = WorkspaceClient()
pg_api = PostgresAPI(w.api_client)

project = pg_api.get_project(name=f"projects/{project_id}")
default_branch = next(iter(pg_api.list_branches(parent=project.name)))
branch_parent = default_branch.name

pg_api.create_role(
    parent=branch_parent,
    role=Role(
        spec=RoleRoleSpec(
            identity_type=RoleIdentityType.SERVICE_PRINCIPAL,
            auth_method=RoleAuthMethod.LAKEBASE_OAUTH_V1,
            postgres_role=client_id,
        )
    ),
    role_id="arxiv-agent-spn",
).wait()

# COMMAND ----------
# Step 4: Postgres role SQL
endpoint = next(iter(pg_api.list_endpoints(parent=branch_parent)))
host = endpoint.status.hosts.host
pg_credential = pg_api.generate_database_credential(endpoint=endpoint.name)

user = w.current_user.me()
username = urllib.parse.quote_plus(user.user_name)

conn_string = (
    f"postgresql://{username}:{pg_credential.token}@{host}:5432/"
    "databricks_postgres?sslmode=require"
)

with psycopg.connect(conn_string) as conn:
    conn.execute(f"""
        GRANT USAGE ON SCHEMA public TO "{client_id}";
    """)
    conn.execute(f"""
        GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE session_messages TO "{client_id}";
    """)
    conn.execute(f"""
        GRANT USAGE, SELECT ON SEQUENCE session_messages_id_seq TO "{client_id}";
    """)
