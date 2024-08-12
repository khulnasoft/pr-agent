## Run as a GitLab Pipeline
You can use a pre-built Action Docker image to run PR-Assistant as a GitLab pipeline. This is a simple way to get started with PR-Assistant without setting up your own server.

(1) Add the following file to your repository under `.gitlab-ci.yml`:
```yaml
stages:
  - pr_assistant

pr_assistant_job:
  stage: pr_assistant
  image: 
    name: khulnasoft/pr-assistant:latest
    entrypoint: [""]
  script:
    - cd /app
    - echo "Running PR Assistant action step"
    - export MR_URL="$CI_MERGE_REQUEST_PROJECT_URL/merge_requests/$CI_MERGE_REQUEST_IID"
    - echo "MR_URL=$MR_URL"
    - export gitlab__PERSONAL_ACCESS_TOKEN=$GITLAB_PERSONAL_ACCESS_TOKEN 
    - export config__git_provider="gitlab"
    - export openai__key=$OPENAI_KEY
    - python -m pr_assistant.cli --pr_url="$MR_URL" describe
    - python -m pr_assistant.cli --pr_url="$MR_URL" review
    - python -m pr_assistant.cli --pr_url="$MR_URL" improve
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_STATE == "opened"'
```
This script will run PR-Assistant on every new merge request. You can modify the `rules` section to run PR-Assistant on different events.
You can also modify the `script` section to run different PR-Assistant commands, or with different parameters by exporting different environment variables.


(2) Add the following masked variables to your GitLab repository (CI/CD -> Variables):

- `GITLAB_PERSONAL_ACCESS_TOKEN`: Your GitLab personal access token.

- `OPENAI_KEY`: Your OpenAI key.

Note that if your base branches are not protected, don't set the variables as `protected`, since the pipeline will not have access to them.



## Run a GitLab webhook server

1. From the GitLab workspace or group, create an access token. Enable the "api" scope only.

2. Generate a random secret for your app, and save it for later. For example, you can use:

```
WEBHOOK_SECRET=$(python -c "import secrets; print(secrets.token_hex(10))")
```
3. Follow the instructions to build the Docker image, setup a secrets file and deploy on your own server from [here](https://pr-assistant-docs.khulnasoft.com/installation/github/#run-as-a-github-app) steps 4-7.

4. In the secrets file, fill in the following:
    - Your OpenAI key.
    - In the [gitlab] section, fill in personal_access_token and shared_secret. The access token can be a personal access token, or a group or project access token.
    - Set deployment_type to 'gitlab' in [configuration.toml](https://github.com/Khulnasoft/pr-assistant/blob/main/pr_assistant/settings/configuration.toml)
   
5. Create a webhook in GitLab. Set the URL to ```http[s]://<PR_AGENT_HOSTNAME>/webhook```. Set the secret token to the generated secret from step 2.
In the "Trigger" section, check the ‘comments’ and ‘merge request events’ boxes.

6. Test your installation by opening a merge request or commenting or a merge request using one of KhulnaSoft's commands.
