import pytest
from unittest.mock import AsyncMock, MagicMock
from arcade_asana.tools.projects import create_project, get_project_details, list_projects

@pytest.fixture
def mock_tool_context():
    context = MagicMock()
    context.http_client = AsyncMock()
    context.authorization = MagicMock()
    context.authorization.token = "fake_token"
    return context

@pytest.mark.asyncio
async def test_create_project(mock_tool_context):
    mock_tool_context.http_client.post.return_value.json.return_value = {
        "data": {"gid": "123", "name": "Test Project"}
    }
    
    result = await create_project(mock_tool_context, "Test Project", "workspace_123")
    
    assert result == {"data": {"gid": "123", "name": "Test Project"}}
    mock_tool_context.http_client.post.assert_called_once()

@pytest.mark.asyncio
async def test_get_project_details(mock_tool_context):
    mock_tool_context.http_client.get.return_value.json.return_value = {
        "data": {"gid": "123", "name": "Test Project", "notes": "Project notes"}
    }
    
    result = await get_project_details(mock_tool_context, "123")
    
    assert result == {"data": {"gid": "123", "name": "Test Project", "notes": "Project notes"}}
    mock_tool_context.http_client.get.assert_called_once()

@pytest.mark.asyncio
async def test_list_projects(mock_tool_context):
    mock_tool_context.http_client.get.return_value.json.return_value = {
        "data": [
            {"gid": "123", "name": "Project 1"},
            {"gid": "456", "name": "Project 2"}
        ]
    }
    
    result = await list_projects(mock_tool_context)
    
    assert result == {
        "data": [
            {"gid": "123", "name": "Project 1"},
            {"gid": "456", "name": "Project 2"}
        ]
    }
    mock_tool_context.http_client.get.assert_called_once()