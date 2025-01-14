# Arcade Asana

An Arcade AI toolkit designed to interact with Asana, enabling users to manage projects, tasks, and collaborate effectively.

## Features

- **Project Management**: Easily create, list and access projects
- **Task Operations**: Create, update, and manage tasks within projects
- **Task Details**: Retrieve detailed information about tasks
- **Task Assignment**: Assign or reassign tasks to team members
- **Task Comments**: Add comments to tasks for better collaboration
- **Secure OAuth Integration**: Built-in secure authentication flow with Asana's OAuth 2.0

## Roadmap

- [ ] Add/update task due dates
- [ ] Add/remove task assignees
- [ ] Implement subtasks management
- [ ] Integrate with Asana's reporting features

## Prerequisites

Before getting started, ensure you have:

- An Asana account with appropriate access levels
- Permission to create and manage Asana apps
- Access to target workspaces and projects

## Configuration

### 1. Create an Asana App

1. Go to the [Asana Developer Console](https://app.asana.com/0/developer-console)
2. Click on "Create new app"
3. Set the redirect URI to: `https://cloud.arcade-ai.com/api/v1/oauth/callback`
4. Save your client ID and secret

### 2. Environment Setup

Add these variables to your `arcade.env`:

```env
ASANA_CLIENT_ID=your_client_id
ASANA_CLIENT_SECRET=your_client_secret
```

### 3. OAuth Configuration

Add this configuration to your Arcade engine setup:

```yaml
auth:
  providers:
    - id: asana
      enabled: true
      type: oauth2
      description: "Asana OAuth 2.0 provider"
      client_id: ${env:ASANA_CLIENT_ID}
      client_secret: ${env:ASANA_CLIENT_SECRET}
      oauth2:
        authorize_request:
          endpoint: "https://app.asana.com/-/oauth_authorize"
          params:
            response_type: "code"
            client_id: "{{client_id}}"
            redirect_uri: "{{redirect_uri}}"
        token_request:
          endpoint: "https://app.asana.com/-/oauth_token"
          params:
            grant_type: "authorization_code"
            redirect_uri: "{{redirect_uri}}"
          auth_method: "client_secret_post"
```

## Usage Examples

### Project Management

```plaintext
# Create a new project
"Create a new project called 'Website Redesign' in the 'Marketing' workspace"

# List accessible projects
"Show me all the projects I have access to"

# Get project details
"What are the details of the project called 'Website Redesign'?"
```

### Task Operations

```plaintext
# Create a new task
"Create a new task called 'Design homepage mockup' in the 'Website Redesign' project, due next Monday"

# Create a new task
"Create a new task called 'Review design mockups' in the 'Website Redesign' project, due next Friday"

# Update task status
"Mark the task 'Design homepage mockup' as complete"

# List tasks
"Show me all incomplete tasks in the 'Marketing Campaign' project"
```

### Task Assignment

```plaintext
# Assign a task
"Assign the task 'Create social media posts' to John Doe"

# Change task assignee
"Reassign the 'Write blog post' task from Jane Smith to Mike Johnson"
```

### Task Comments

```plaintext
# Add a comment
"Add a comment to the 'Prepare presentation' task: 'First draft is ready for review'"

# Retrieve task comments
"Show me all comments on the 'Client meeting preparation' task"
```