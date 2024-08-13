
## Getting Started with PR-Insight Pro

PR-Insight Pro is a versatile application compatible with GitHub, GitLab, and BitBucket, hosted by KhulnaSoftAI.
See [here](https://pr-insight-docs.khulnasoft.com/#pr-insight-pro) for more details about the benefits of using PR-Insight Pro.

Interested parties can subscribe to PR-Insight Pro through the following [link](https://www.khulnasoft.com/pricing/). 
After subscribing, you are granted the ability to easily install the application across any of your repositories.

![PR Insight Pro](https://khulnasoft.com/images/pr_insight/pr_insight_pro_install.png){width=468}

Each user who wants to use PR-Insight pro needs to buy a seat. 
Initially, KhulnaSoftAI offers a two-week trial period at no cost, after which continued access requires each user to secure a personal seat.
Once a user acquires a seat, they gain the flexibility to use PR-Insight Pro across any repository where it was enabled.

Users without a purchased seat who interact with a repository featuring PR-Insight Pro are entitled to receive up to five complimentary feedbacks.
Beyond this limit, PR-Insight Pro will cease to respond to their inquiries unless a seat is purchased.

## Install PR-Insight Pro for GitHub Enterprise Server
You can install PR-Insight Pro application on your GitHub Enterprise Server, and enjoy two weeks of free trial.
After the trial period, to continue using PR-Insight Pro, you will need to contact us for an [Enterprise license](https://www.khulnasoft.com/pricing/).


## Install PR-Insight Pro for GitLab (Teams & Enterprise)

Since GitLab platform does not support apps, installing PR-Insight Pro for GitLab is a bit more involved, and requires the following steps:

### Step 1

Acquire a personal, project or group level access token. Enable the “api” scope in order to allow PR-Insight to read pull requests, comment and respond to requests.

<figure markdown="1">
![Step 1](https://www.khulnasoft.com/images/pr_insight/gitlab_pro_pat.png){width=750}
</figure>

Store the token in a safe place, you won’t be able to access it again after it was generated.

### Step 2

Generate a shared secret and link it to the access token. Browse to [https://register.gitlab.pr-insight.khulnasoft.com](https://register.gitlab.pr-insight.khulnasoft.com).
Fill in your generated GitLab token and your company or personal name in the appropriate fields and click "Submit".

You should see "Success!" displayed above the Submit button, and a shared secret will be generated. Store it in a safe place, you won’t be able to access it again after it was generated.

### Step 3

Install a webhook for your repository or groups, by clicking “webhooks” on the settings menu. Click the “Add new webhook” button.

<figure markdown="1">
![Step 3.1](https://www.khulnasoft.com/images/pr_insight/gitlab_pro_add_webhook.png)
</figure>

In the webhook definition form, fill in the following fields:
URL: https://pro.gitlab.pr-insight.khulnasoft.com/webhook

Secret token: Your KhulnaSoftAI key
Trigger: Check the ‘comments’ and ‘merge request events’ boxes.
Enable SSL verification: Check the box.

<figure markdown="1">
![Step 3.2](https://www.khulnasoft.com/images/pr_insight/gitlab_pro_webhooks.png){width=750}
</figure>

### Step 4

You’re all set!

Open a new merge request or add a MR comment with one of PR-Insight’s commands such as /review, /describe or /improve.