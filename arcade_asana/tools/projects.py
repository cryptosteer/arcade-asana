from typing import Annotated, Dict, Optional
from arcade.sdk import ToolContext, tool
from arcade.sdk.auth import OAuth2
from .asana_api import create_project_api, list_projects_api, get_project_details_api, AsanaError

@tool(requires_auth=OAuth2(provider_id="asana"))
async def create_project(
    context: ToolContext,
    name: Annotated[str, "The name of the project"],
    workspace_gid: Annotated[str, "The globally unique identifier for the workspace"],
    team_gid: Annotated[Optional[str], "The globally unique identifier for the team"] = None,
    notes: Annotated[Optional[str], "Any notes about the project"] = None,
    color: Annotated[Optional[str], "The color of the project"] = None,
    due_date: Annotated[Optional[str], "The date on which this project is due (YYYY-MM-DD)"] = None
) -> Annotated[dict[str, Dict],
    "A dictionary with key 'project' containing the created project details"]:
    """Create a new project in the specified workspace"""
    try:
        if context.authorization is None:
            raise AsanaError("Authorization is required")

        token = (
            context.authorization.token if context.authorization and context.authorization.token else ""
        )
        
        project_data = {
            "name": name,
            "workspace": workspace_gid
        }
        
        if team_gid:
            project_data["team"] = team_gid
        if notes:
            project_data["notes"] = notes
        if color:
            project_data["color"] = color
        if due_date:
            project_data["due_date"] = due_date

        result = create_project_api(token, project_data)
        if result["error"]:
            raise AsanaError(f"Failed to create project: {result['error']}")
        
        project = result["data"].get("data", {})
        return {"project": project}
    except Exception as e:
        raise AsanaError(f"Failed to create project: {str(e)}")

@tool(requires_auth=OAuth2(provider_id="asana"))
async def list_projects(
    context: ToolContext
) -> Annotated[dict[str, list[dict]],
    "A dictionary with key 'projects' containing a list of projects"]:
    """List all projects accessible to the authenticated user in the specified workspace"""
    try:
        if context.authorization is None:
            raise AsanaError("Authorization is required")

        token = (
            context.authorization.token if context.authorization and context.authorization.token else ""
        )        
        result = list_projects_api(token)
        if result["error"]:
            raise AsanaError(f"Failed to list projects: {result['error']}")
        
        projects = result["data"].get("data", [])
        return {"projects": projects}
    except Exception as e:
        raise AsanaError(f"Failed to list projects: {str(e)}")


@tool(requires_auth=OAuth2(provider_id="asana"))
async def get_project_details(
    context: ToolContext,
    project_gid: Annotated[str, "Globally unique identifier for the project"]
) -> Annotated[dict[str, dict],
    "A dictionary with key 'project' containing the project details"]:
    """Get the complete project record for a single project"""
    try:
        if context.authorization is None:
            raise AsanaError("Authorization is required")

        token = (
            context.authorization.token if context.authorization and context.authorization.token else ""
        )
        result = get_project_details_api(token, project_gid)
        if result["error"]:
            raise AsanaError(f"Failed to get project details: {result['error']}")
        
        project = result["data"].get("data", {})
        return {"project": project}
    except Exception as e:
        raise AsanaError(f"Failed to get project details: {str(e)}")
