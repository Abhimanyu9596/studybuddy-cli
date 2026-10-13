# Contributing to StudyBuddy CLI

Thanks for helping out! This is how changes flow into the project.

## 1. Find or open an issue

- Browse the **Issues** tab. Issues labelled `good first issue` are a good start.
- Found a bug or have an idea? Open a new issue using the bug report or feature request template.
- Comment on an issue to say you are working on it, so nobody duplicates the effort.

## 2. Fork and clone

```bash
git clone https://github.com/<your-username>/studybuddy-cli.git
cd studybuddy-cli
```

## 3. Create a branch

Use a short, descriptive name that includes the issue number:

```bash
git checkout -b fix/date-format-crash-1
```

Prefixes: `fix/` for bugs, `feat/` for features, `docs/` for documentation, `test/` for tests.

## 4. Make your change

- Keep changes small and focused on one issue.
- Follow PEP 8 style.
- Add or update tests in `tests/` for any behaviour you change.
- Run the tests before committing:

```bash
python -m unittest discover tests
```

## 5. Commit

Write clear commit messages in the imperative mood:

```
Accept DD-MM-YYYY dates in parse_date

Closes #1
```

## 6. Open a Pull Request

- Push your branch and open a PR against `main`.
- Fill in the PR template and link the issue with `Closes #<number>`.
- Describe what changed, why, and how you tested it.

## 7. Review process

1. At least **one other team member** must review the PR.
2. Reviewers leave comments on specific lines or approve the PR.
3. The author addresses comments with further commits on the same branch.
4. Once approved and tests pass, a maintainer merges the PR (squash merge).
5. The linked issue closes automatically.

## Code of conduct

Be respectful and constructive. Review the code, not the person.
