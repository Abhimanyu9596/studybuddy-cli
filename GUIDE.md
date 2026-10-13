# StudyBuddy CLI: Step-by-Step Guide for the Group

This guide takes you from zero to a finished CA-3 case study. Do the steps in order.

Roles:
- **Student 1:** Project & Repository
- **Student 2:** Issue & Bug Investigation
- **Student 3:** Contribution & Pull Request

---

## PART A: One-time setup (everyone)

### A1. Install the tools
1. **Python 3.8+**: https://www.python.org/downloads/ (tick "Add Python to PATH" on Windows).
2. **Git**: https://git-scm.com/downloads
3. A code editor: **VS Code** (https://code.visualstudio.com).
4. Check in a terminal:
   ```bash
   python --version
   git --version
   ```

### A2. Create GitHub accounts
All three students create a free account at https://github.com.

### A3. Tell Git who you are
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
Use the same email as your GitHub account.

---

## PART B: Student 1: Create the repository

### B1. Create the repo on GitHub
1. Click **+ → New repository**.
2. Name: `studybuddy-cli`. Visibility: **Public**.
3. Do NOT tick "Add a README" (you already have one). Click **Create repository**.

### B2. Push the starter files
Unzip the starter project, open a terminal inside the `studybuddy-cli` folder, then:
```bash
git init
git add .
git commit -m "Initial commit: StudyBuddy CLI v0.1"
git branch -M main
git remote add origin https://github.com/<your-username>/studybuddy-cli.git
git push -u origin main
```

### B3. Add your teammates
Repo → **Settings → Collaborators → Add people** → add Student 2 and Student 3.

### B4. Take screenshots (evidence)
- Repo home page, the file list, README rendered, the commit history.
- Run the app and screenshot each command working:
  ```bash
  python studybuddy.py add "OST assignment" --due 2026-10-20
  python studybuddy.py list
  python studybuddy.py due-soon --days 30
  python studybuddy.py export tasks.csv
  ```

### B5. Document the repository (for your report section)
Explain: what the project does, each file's purpose, the license, and the commit/issue activity so far.

---

## PART C: Student 2: Issues and the bug

### C1. Clone the repo
```bash
git clone https://github.com/<student1-username>/studybuddy-cli.git
cd studybuddy-cli
```

### C2. Reproduce the bug (the app has a known one)
```bash
python studybuddy.py add "Test task" --due 13-10-2026
```
**Expected:** the task is added, or a friendly message like "Please use YYYY-MM-DD".
**Actual:** a Python traceback ending in `ValueError: time data '13-10-2026' does not match format '%Y-%m-%d'`.

Record: OS, Python version, exact command, expected result, actual result, screenshot of the terminal.

### C3. Create the issues on GitHub
Repo → **Issues → New issue**. Use the bug report template for the first one.

| # | Title | Label |
|---|-------|-------|
| 1 | Crash on DD-MM-YYYY date | bug |
| 2 | Accept both DD-MM-YYYY and YYYY-MM-DD dates | enhancement |
| 3 | Add `--priority` option (high/medium/low) | enhancement |
| 4 | Add unit test for invalid date input | good first issue |
| 5 | `due-soon` crashes if tasks.json has a bad date | bug |
| 6 | Improve README with usage screenshots | documentation |

Create labels under **Issues → Labels** if they are missing (`bug`, `enhancement`, `documentation`, `good first issue`).

### C4. Investigate Issue #1
Comment on it with your findings: root cause (`parse_date` in `studybuddy.py` only accepts one format and nothing catches `ValueError`), affected commands (`add`), and a proposed fix. Screenshot the issue page and the discussion.

### C5. Document for the report
Environment, steps, expected vs actual, evidence, root cause, and final status (open → closed by PR).

---

## PART D: Student 3: Contribution workflow and Pull Requests

### D1. Read the contribution files
Open `CONTRIBUTING.md`, `.github/pull_request_template.md` and the issue templates. In your report, explain the workflow: issue → branch → change → PR → review → merge.

### D2. Fix the bug on a branch
```bash
git clone https://github.com/<student1-username>/studybuddy-cli.git
cd studybuddy-cli
git checkout -b fix/date-format-crash-1
```

Edit `parse_date` in `studybuddy.py`:
```python
def parse_date(text):
    """Accept YYYY-MM-DD or DD-MM-YYYY."""
    for fmt in ("%Y-%m-%d", "%d-%m-%Y"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Invalid date '{text}'. Use YYYY-MM-DD or DD-MM-YYYY.")
```

And make `main` show a clean message instead of a traceback for the `add` command:
```python
    if args.command == "add":
        try:
            task = add_task(args.title, args.due)
        except ValueError as e:
            print(f"Error: {e}")
            return
        print(f"Added task {task['id']}: {task['title']} (due {task['due']})")
```

Add tests in `tests/test_studybuddy.py` (inside the class):
```python
    def test_parse_date_both_formats(self):
        self.assertEqual(studybuddy.parse_date("2026-10-13"), studybuddy.parse_date("13-10-2026"))

    def test_parse_date_invalid(self):
        with self.assertRaises(ValueError):
            studybuddy.parse_date("not-a-date")
```

Run the tests:
```bash
python -m unittest discover tests
```

### D3. Commit and push
```bash
git add .
git commit -m "Accept DD-MM-YYYY dates and show friendly error

Closes #1"
git push -u origin fix/date-format-crash-1
```
(If you are a collaborator, this works directly. Otherwise fork the repo first.)

### D4. Open the Pull Request
1. GitHub shows a **Compare & pull request** button. Click it.
2. Fill in the template, include `Closes #1`.
3. Request **Student 2** as reviewer.

### D5. Review (Student 2 does this)
PR → **Files changed** → click `+` next to a line to comment → **Review changes → Approve** (or Request changes).

### D6. Merge
After approval, Student 1 clicks **Squash and merge**. Issue #1 closes automatically. Screenshot the PR, the review comments, the "Merged" status and the closed issue.

### D7. Second PR
Repeat D2 to D6 for issue #3 (`--priority` feature) so you have two PRs. Student 2 or 1 can author this one so everyone has hands-on Git evidence.

---

## PART E: Report and presentations

### E1. Report structure (from the guidelines)
Title Page → Introduction → Project Overview → Repository Investigation → Issue Investigation → Bug Investigation → Contribution Process → Pull Request Investigation → Practical Observations → Changes/Contribution → Conclusion → References.

Each student writes their own sections; all three read the full report.

### E2. First presentation (8 marks): suggested slides
1. Title, group number, names, roll numbers, repo link
2. Project purpose and features
3. Repository structure (screenshot)
4. Issue and bug found (screenshots)
5. Reproduction steps and result
6. Proposed contribution (the fix and the priority feature)
7. Work completed so far and the GitHub activity page

Remember the rubric: push regularly to GitHub (2 marks), submit on time (1 mark), and show something original (3 marks, the `--priority` feature and tests count here).

### E3. Final presentation and viva (7 marks)
- **Live demo:** reproduce the bug on the old version (`git checkout <first-commit>`), then show it fixed on `main`.
- Show the PR, review comments and merged status.
- **Viva prep:** every member must be able to explain the whole project, including how `parse_date` works, what a branch and a PR are, and why you chose the MIT license.

---

## Weekly plan (adjust to your deadline)

| When | Task |
|------|------|
| Day 1 | Part A and B, repo live, submit group and project details |
| Day 2 | Part C, issues created, bug reproduced |
| Day 3 | Part D, first PR reviewed and merged |
| Day 4 | Second PR (`--priority`), more commits |
| Day 5 | First presentation slides |
| After | Report, final demo, viva practice |

## Common problems
- **`git push` asks for a password:** GitHub no longer accepts passwords. Sign in through the browser prompt, or use GitHub Desktop, or create a personal access token under Settings → Developer settings.
- **`python` not found:** try `python3`, or reinstall Python with "Add to PATH" ticked.
- **Merge conflict:** two people edited the same lines. Open the file, keep the right version, remove the `<<<<<<<` markers, then `git add` and `git commit`.
