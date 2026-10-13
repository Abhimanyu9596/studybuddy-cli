# StudyBuddy CLI

A tiny command-line task and deadline tracker for students, written in Python (no external dependencies).

Built as a case study for **Open Source Technologies (TE7756)**, CA-3, Symbiosis Institute of Technology, Pune.

## Features

- Add, list, complete and delete tasks
- `due-soon` shows tasks due in the next N days
- Tasks are stored in a local `tasks.json` file
- Export all tasks to CSV

## Requirements

- Python 3.8 or newer

## Quick start

```bash
git clone https://github.com/<your-username>/studybuddy-cli.git
cd studybuddy-cli

python studybuddy.py add "OST assignment" --due 2026-10-20
python studybuddy.py list
python studybuddy.py done 1
python studybuddy.py due-soon --days 3
python studybuddy.py export tasks.csv
python studybuddy.py delete 1
```

Use `python3` instead of `python` on Linux/macOS if needed.

## Running the tests

```bash
python -m unittest discover tests
```

## Project structure

```
studybuddy-cli/
├── studybuddy.py          # the application
├── tests/
│   └── test_studybuddy.py # unit tests
├── .github/
│   ├── ISSUE_TEMPLATE/    # bug report and feature request templates
│   └── pull_request_template.md
├── CONTRIBUTING.md        # how to contribute
├── LICENSE                # MIT
└── README.md
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request.

## License

MIT, see [LICENSE](LICENSE).
