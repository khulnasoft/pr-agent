# Overview

KhulnaSoft PR-Insight is an open-source tool to help efficiently review and handle pull requests.

- See the [Installation Guide](./installation/index.md) for instructions on installing and running the tool on different git platforms.

- See the [Usage Guide](./usage-guide/index.md) for instructions on running the PR-Insight commands via different interfaces, including _CLI_, _online usage_, or by _automatically triggering_ them when a new PR is opened.

- See the [Tools Guide](./tools/index.md) for a detailed description of the different tools.


## PR-Insight Docs Smart Search

To search the documentation site using natural language:

1) Comment `/help "your question"` in either:

   - A pull request where PR-Insight is installed
   - A [PR Chat](https://pr-insight-docs.khulnasoft.com/chrome-extension/features/#pr-chat)

2) PR-Insight will respond with an [answer](https://github.com/Khulnasoft/pr-insight/pull/1241#issuecomment-2365259334) that includes relevant documentation links.


## PR-Insight Features

PR-Insight offers extensive pull request functionalities across various git providers.

|       |                                                                                                                       | GitHub | Gitlab | Bitbucket | Azure DevOps |
|-------|-----------------------------------------------------------------------------------------------------------------------|:------:|:------:|:---------:|:------------:|
| TOOLS | Review                                                                                                                |   ✅    |   ✅    |   ✅       |      ✅      |
|       | ⮑ Incremental                                                                                                         |   ✅    |        |            |              |
|       | Ask                                                                                                                   |   ✅    |   ✅    |   ✅        |      ✅      |
|       | Describe                                                                                                              |   ✅    |   ✅    |   ✅        |      ✅      |
|       | ⮑ [Inline file summary](https://pr-insight-docs.khulnasoft.com/tools/describe/#inline-file-summary){:target="_blank"} 💎     |   ✅    |   ✅    |           |      ✅      |
|       | Improve                                                                                                               |   ✅    |   ✅    |   ✅        |      ✅      |
|       | ⮑ Extended                                                                                                            |   ✅    |   ✅    |   ✅        |      ✅      |
|       | [Custom Prompt](./tools/custom_prompt.md){:target="_blank"} 💎                                                        |   ✅    |   ✅    |   ✅        |      ✅      |
|       | Reflect and Review                                                                                                    |   ✅    |   ✅    |   ✅        |      ✅      |
|       | Update CHANGELOG.md                                                                                                   |   ✅    |   ✅    |   ✅        |      ️       |
|       | Find Similar Issue                                                                                                    |   ✅    |        |             |      ️       |
|       | [Add PR Documentation](./tools/documentation.md){:target="_blank"} 💎                                                 |   ✅    |   ✅    |          |      ✅      |
|       | [Generate Custom Labels](./tools/describe.md#handle-custom-labels-from-the-repos-labels-page-💎){:target="_blank"} 💎 |   ✅    |   ✅    |            |      ✅      |
|       | [Analyze PR Components](./tools/analyze.md){:target="_blank"} 💎                                                      |   ✅    |   ✅    |       |      ✅      |
|       |                                                                                                                       |        |        |            |      ️       |
| USAGE | CLI                                                                                                                   |   ✅    |   ✅    |   ✅       |      ✅      |
|       | App / webhook                                                                                                         |   ✅    |   ✅    |    ✅        |      ✅      |
|       | Actions                                                                                                               |   ✅    |        |            |      ️       |
|       |                                                                                                                       |        |        |            |
| CORE  | PR compression                                                                                                        |   ✅    |   ✅    |   ✅       |   ✅        |
|       | Repo language prioritization                                                                                          |   ✅    |   ✅    |   ✅       |   ✅        |
|       | Adaptive and token-aware file patch fitting                                                                           |   ✅    |   ✅    |   ✅     |   ✅        |
|       | Multiple models support                                                                                               |   ✅    |   ✅    |   ✅       |   ✅        |
|       | Incremental PR review                                                                                                 |   ✅    |        |            |           |
|       | [Static code analysis](./tools/analyze.md/){:target="_blank"} 💎                                                      |   ✅    |   ✅     |    ✅    |   ✅        |
|       | [Multiple configuration options](./usage-guide/configuration_options.md){:target="_blank"} 💎                         |   ✅    |   ✅     |    ✅    |   ✅        |

💎 marks a feature available only in [PR-Insight Pro](https://www.khulnasoft.com/pricing/){:target="_blank"}


## Example Results
<hr>

#### [/describe](https://github.com/Khulnasoft/pr-insight/pull/530)
<figure markdown="1">
![/describe](https://www.khulnasoft.com/images/pr_insight/describe_new_short_main.png){width=512}
</figure>
<hr>

#### [/review](https://github.com/Khulnasoft/pr-insight/pull/732#issuecomment-1975099151)
<figure markdown="1">
![/review](https://www.khulnasoft.com/images/pr_insight/review_new_short_main.png){width=512}
</figure>
<hr>

#### [/improve](https://github.com/Khulnasoft/pr-insight/pull/732#issuecomment-1975099159)
<figure markdown="1">
![/improve](https://www.khulnasoft.com/images/pr_insight/improve_new_short_main.png){width=512}
</figure>
<hr>

#### [/generate_labels](https://github.com/Khulnasoft/pr-insight/pull/530)
<figure markdown="1">
![/generate_labels](https://www.khulnasoft.com/images/pr_insight/geneare_custom_labels_main_short.png){width=300}
</figure>
<hr>

## How it Works

The following diagram illustrates PR-Insight tools and their flow:

![PR-Insight Tools](https://khulnasoft.com/images/pr_insight/diagram-v0.9.png)

Check out the [PR Compression strategy](core-abilities/index.md) page for more details on how we convert a code diff to a manageable LLM prompt
