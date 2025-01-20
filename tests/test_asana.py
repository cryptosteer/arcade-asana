import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from arcade_asana.tools.projects import create_project, get_project_details, list_projects

@pytest.fixture
def mock_tool_context():
    context = MagicMock()
    context.http_client = AsyncMock()
    context.authorization = MagicMock()
    context.authorization.token = "fake_token"
    return context

@pytest.mark.asyncio
@patch('arcade_asana.tools.projects.create_project_api')
async def test_create_project(mock_create_project_api, mock_tool_context):
    mock_create_project_api.return_value = {
        "data": {"data": {"gid": "123", "name": "Test Project"}},
        "error": None
    }
    
    result = await create_project(mock_tool_context, "Test Project", "workspace_123")
    
    assert result == {"project": {"gid": "123", "name": "Test Project"}}
    mock_create_project_api.assert_called_once_with("fake_token", {
        "name": "Test Project",
        "workspace": "workspace_123"
    })

@pytest.mark.asyncio
@patch('arcade_asana.tools.projects.get_project_details_api')
async def test_get_project_details(mock_get_project_details_api, mock_tool_context):
    mock_get_project_details_api.return_value = {
        "data": {"data": {"gid": "123", "name": "Test Project", "notes": "Project notes"}},
        "error": None
    }
    
    result = await get_project_details(mock_tool_context, "123")
    
    assert result == {"project": {"gid": "123", "name": "Test Project", "notes": "Project notes"}}
    mock_get_project_details_api.assert_called_once_with("fake_token", "123")

@pytest.mark.asyncio
@patch('arcade_asana.tools.projects.list_projects_api')
async def test_list_projects(mock_list_projects_api, mock_tool_context):
    mock_list_projects_api.return_value = {
        "data": {"data": [
            {"gid": "123", "name": "Project 1"},
            {"gid": "456", "name": "Project 2"}
        ]},
        "error": None
    }
    
    result = await list_projects(mock_tool_context)
    
    assert result == {
        "projects": [
            {"gid": "123", "name": "Project 1"},
            {"gid": "456", "name": "Project 2"}
        ]
    }
    mock_list_projects_api.assert_called_once_with("fake_token")