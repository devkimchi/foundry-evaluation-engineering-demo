# Contributing

Thank you for helping improve this Microsoft Foundry evaluation demo.

## Code of Conduct

By participating, you agree to follow the
[Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md).

## Ways to Contribute

- Correct inaccurate or unclear documentation.
- Improve the portal demo runbook and result interpretation guidance.
- Add realistic evaluation scenarios without including confidential data.
- Improve accessibility, screenshots, or translations.

## Development Workflow

1. Fork and clone the repository.
2. Create a branch using `feat/`, `fix/`, or `docs/`.
3. Edit the Markdown, prompt, or JSONL assets.
4. Keep examples fictional and remove personal or organization-sensitive data.
5. Run the repository checks through the generated CI workflow.
6. Open a pull request and explain the learner-facing impact.

## Dataset Changes

Each line in `demo/evaluation-dataset.jsonl` must remain valid JSON. Keep
scenarios focused on agent evaluation, with one test case per line. Do not add
production prompts, credentials, customer data, or proprietary policy text.

## Commit Convention

Use [Conventional Commits](https://www.conventionalcommits.org/):

- `docs:` documentation-only changes
- `fix:` corrections to demo assets or guidance
- `feat:` new scenarios or learning material
- `chore:` repository maintenance

## Issues and Pull Requests

Use the provided issue forms for bugs and feature requests. Pull requests
should link related issues, describe the change, and confirm that Markdown and
JSONL validation passes.
