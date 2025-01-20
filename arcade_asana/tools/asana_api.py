import requests
from typing import Dict, Any

ASANA_BASE_URL = "https://app.asana.com/api/1.0"

class AsanaError(Exception):
    """Custom exception for Asana-related errors"""
    pass

def get_headers(token: str) -> Dict[str, str]:
    """Generate headers for Asana API requests."""
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

def create_project_api(token: str, project_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a new project using the Asana API.

    Args:
        token (str): The OAuth2 token for authentication.
        project_data (Dict[str, Any]): The data for creating the project.

    Returns:
        Dict[str, Any]: A dictionary containing the API response with created project details or error information.
    """
    endpoint = "/projects"
    url = f"{ASANA_BASE_URL}{endpoint}"
    headers = get_headers(token)


    try:
        response = requests.post(url, json={"data": project_data}, headers=headers)
        response.raise_for_status()
        return {"error": None, "data": response.json()}
    except requests.RequestException as e:
        return {"error": str(e), "data": None}

def list_projects_api(token: str) -> Dict[str, Any]:
    """
    List projects in a workspace.

    Args:
        token: Asana API token
        archived: (optional) Only return projects whose archived field matches this value
        workspace: (optional) The workspace to filter projects on

    Returns:
        Dictionary with response data or error message
    """
    endpoint = "/projects"
    params: Dict[str, Any] = {}

    url = f"{ASANA_BASE_URL}{endpoint}"
    headers = get_headers(token)

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return {"data": response.json(), "error": None}
    except requests.RequestException as e:
        return {"data": None, "error": str(e)}

def get_project_details_api(token: str, project_gid: str) -> Dict:
    """
    Fetch details of a specific project from Asana API.

    Args:
        token (str): The OAuth2 token for authentication.
        project_gid (str): The globally unique identifier for the project.

    Returns:
        Dict: A dictionary containing the API response with project details or error information.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    url = f"{ASANA_BASE_URL}/projects/{project_gid}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return {"error": None, "data": response.json()}
    except requests.RequestException as e:
        return {"error": str(e), "data": None}
    