# Arcade Asana

An Arcade AI toolkit designed to interact with Asana, enabling users to manage projects, tasks, and collaborate effectively.

## Features

- **Project Management**: Easily create, list and access projects
- **Secure OAuth Integration**: Built-in secure authentication flow with Asana's OAuth 2.0

## Roadmap

- [ ] Create, update, and manage tasks within projects
- [ ] Retrieve detailed information about tasks
- [ ] Add/remove task assignees
- [ ] Add/update task due dates
- [ ] Add comments to tasks for better collaboration
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
5. Go to "Manage distribution" section
6. Choose distribution method "Any workspace" and click on "Save changes"

### 2. Environment Setup

Add these variables to your `arcade.env`:

```env
ASANA_CLIENT_ID=your_client_id
ASANA_CLIENT_SECRET=your_client_secret
```

Add to asana provider to your :

### 3. OAuth Configuration

Add this configuration to your Arcade engine setup file `engine.yaml`:

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
            scope: "default"
        token_request:
          endpoint: "https://app.asana.com/-/oauth_token"
          params:
            grant_type: "authorization_code"
            redirect_uri: "{{redirect_uri}}"
          auth_method: "client_secret_basic"
```

You can find detailed instructions on locating and configuring the engine file at: `https://docs.arcade-ai.com/home/install/local#engine-config-not-found`.

## Usage Examples

### Project Management

```plaintext
# Create a new project
"Please create a new project in Asana titled 'Website Redesign' in the Default Workspace with dark blue as the theme color, and add 'Complete website redesign project' as the project description."

# List accessible projects
"Show me all the projects I have access to"

# Get project details
"What are the details of the project called 'Website Redesign'?"
```