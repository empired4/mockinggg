import os
import httpx
import uuid
from jinja2 import Environment, FileSystemLoader
from config import CLASSPLUS_API_BASE, TMP_DIR

env = Environment(loader=FileSystemLoader("templates"))

# Simulated API endpoints (Replace with real Classplus API endpoints)
LOGIN_ORG_CODE_URL = f"{CLASSPLUS_API_BASE}/login/orgcode"
LOGIN_TOKEN_URL = f"{CLASSPLUS_API_BASE}/login/token"
FETCH_MOCKS_URL = f"{CLASSPLUS_API_BASE}/mocks"
FETCH_MOCK_DETAIL_URL = f"{CLASSPLUS_API_BASE}/mock"

def ensure_tmp_dir():
    if not os.path.exists(TMP_DIR):
        os.makedirs(TMP_DIR)

async def login_with_org_code(org_code: str, username: str, password: str):
    """
    Simulate login with organisation code + credentials.
    Returns auth token or raises Exception.
    """
    # Replace with actual API call
    async with httpx.AsyncClient() as client:
        resp = await client.post(LOGIN_ORG_CODE_URL, json={
            "org_code": org_code,
            "username": username,
            "password": password
        })
        if resp.status_code != 200:
            raise Exception("Invalid organisation code or credentials")
        data = resp.json()
        return data.get("auth_token")

async def login_with_token(token: str):
    """
    Validate token (simulate).
    """
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{LOGIN_TOKEN_URL}?token={token}")
        if resp.status_code != 200:
            raise Exception("Invalid authorization token")
        return token

async def fetch_mock_list(auth_token: str):
    """
    Fetch list of mocks for the user.
    Returns list of dicts: [{"id": "101", "name": "SSC CGL Tier 1 Mock 1"}, ...]
    """
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {auth_token}"}
        resp = await client.get(FETCH_MOCKS_URL, headers=headers)
        if resp.status_code != 200:
            raise Exception("Failed to fetch mock tests")
        return resp.json().get("mocks", [])

async def fetch_mock_details(auth_token: str, mock_id: str):
    """
    Fetch mock test details including questions, options, images, explanations.
    Returns dict with mock info and questions.
    """
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {auth_token}"}
        resp = await client.get(f"{FETCH_MOCK_DETAIL_URL}/{mock_id}", headers=headers)
        if resp.status_code != 200:
            raise Exception("Invalid mock ID or failed to fetch mock details")
        return resp.json()

def generate_mock_html(mock_data: dict):
    """
    Render mock HTML using Jinja2 template.
    Returns path to generated HTML file.
    """
    ensure_tmp_dir()
    template = env.get_template("mock_template.html")
    html_content = template.render(mock=mock_data)

    filename = f"{mock_data['name'].replace(' ', '_')}_{uuid.uuid4().hex[:8]}.html"
    filepath = os.path.join(TMP_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)

    return filepath

def cleanup_file(filepath: str):
    if os.path.exists(filepath):
        os.remove(filepath)
