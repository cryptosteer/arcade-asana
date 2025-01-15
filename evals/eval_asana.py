from arcade.sdk import ToolCatalog
from arcade.sdk.eval import (
    EvalRubric,
    EvalSuite,
    SimilarityCritic,
    tool_eval,
)

import arcade_asana
from arcade_asana.tools.projects import create_project, get_project_details, list_projects

# Evaluation rubric
rubric = EvalRubric(
    fail_threshold=0.85,
    warn_threshold=0.95,
)

catalog = ToolCatalog()
catalog.add_module(arcade_asana)

@tool_eval()
def asana_eval_suite() -> EvalSuite:
    suite = EvalSuite(
        name="Asana Projects Tools Evaluation",
        system_message=(
            "You are an AI assistant with access to Asana project management tools. "
            "Use them to help the user manage their projects."
        ),
        catalog=catalog,
        rubric=rubric,
    )

    suite.add_case(
        name="Creating a project",
        user_message="Can you create a new project called 'Website Redesign'?",
        expected_tool_calls=[(create_project, {"name": "Website Redesign"})],
        rubric=rubric,
        critics=[
            SimilarityCritic(critic_field="name", weight=0.5),
        ],
    )

    suite.add_case(
        name="Getting project details",
        user_message="What are the details of the 'Marketing Campaign' project?",
        expected_tool_calls=[(get_project_details, {"project_id": "123456"})],
        rubric=rubric,
        critics=[
            SimilarityCritic(critic_field="project_id", weight=0.5),
        ],
        additional_messages=[
            {"role": "user", "content": "The project ID for 'Marketing Campaign' is 123456."},
            {"role": "assistant", "content": "Certainly! I'll retrieve the details of the 'Marketing Campaign' project for you."},
        ],
    )

    suite.add_case(
        name="Listing projects",
        user_message="Can you show me a list of all my current projects?",
        expected_tool_calls=[(list_projects, {})],
        rubric=rubric,
    )

    return suite 