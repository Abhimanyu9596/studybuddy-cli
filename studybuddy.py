"""StudyBuddy CLI - a tiny task and deadline tracker for students.

Usage examples:
    python studybuddy.py add "OST assignment" --due 2026-10-20
    python studybuddy.py list
    python studybuddy.py done 1
    python studybuddy.py delete 1
    python studybuddy.py due-soon --days 3
    python studybuddy.py export tasks.csv
"""

import argparse
import csv
import json
import os
from datetime import date, datetime, timedelta

DATA_FILE = os.environ.get("STUDYBUDDY_FILE", "tasks.json")


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def parse_date(text):
    # NOTE: this only accepts YYYY-MM-DD and raises ValueError otherwise.
    # (Known bug - see the "Crash on DD-MM-YYYY date" issue.)
    return datetime.strptime(text, "%Y-%m-%d").date()


def next_id(tasks):
    return max((t["id"] for t in tasks), default=0) + 1


def add_task(title, due):
    tasks = load_tasks()
    due_date = parse_date(due)
    task = {
        "id": next_id(tasks),
        "title": title,
        "due": due_date.isoformat(),
        "done": False,
    }
    tasks.append(task)
    save_tasks(tasks)
    return task


def list_tasks():
    return sorted(load_tasks(), key=lambda t: t["due"])


def mark_done(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            return True
    return False


def delete_task(task_id):
    tasks = load_tasks()
    remaining = [t for t in tasks if t["id"] != task_id]
    if len(remaining) == len(tasks):
        return False
    save_tasks(remaining)
    return True


def due_soon(days=3):
    today = date.today()
    limit = today + timedelta(days=days)
    result = []
    for t in load_tasks():
        d = parse_date(t["due"])
        if not t["done"] and today <= d <= limit:
            result.append(t)
    return sorted(result, key=lambda t: t["due"])


def export_csv(path):
    tasks = load_tasks()
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "due", "done"])
        writer.writeheader()
        writer.writerows(tasks)
    return len(tasks)


def print_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        mark = "x" if t["done"] else " "
        print(f"[{mark}] {t['id']:>3}  {t['due']}  {t['title']}")


def build_parser():
    parser = argparse.ArgumentParser(prog="studybuddy", description="Track study tasks and deadlines.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add a task")
    p_add.add_argument("title")
    p_add.add_argument("--due", required=True, help="Due date, format YYYY-MM-DD")

    sub.add_parser("list", help="List all tasks")

    p_done = sub.add_parser("done", help="Mark a task as done")
    p_done.add_argument("id", type=int)

    p_del = sub.add_parser("delete", help="Delete a task")
    p_del.add_argument("id", type=int)

    p_soon = sub.add_parser("due-soon", help="Show tasks due soon")
    p_soon.add_argument("--days", type=int, default=3)

    p_exp = sub.add_parser("export", help="Export tasks to CSV")
    p_exp.add_argument("path")

    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)

    if args.command == "add":
        task = add_task(args.title, args.due)
        print(f"Added task {task['id']}: {task['title']} (due {task['due']})")
    elif args.command == "list":
        print_tasks(list_tasks())
    elif args.command == "done":
        print("Marked done." if mark_done(args.id) else f"No task with id {args.id}.")
    elif args.command == "delete":
        print("Deleted." if delete_task(args.id) else f"No task with id {args.id}.")
    elif args.command == "due-soon":
        print_tasks(due_soon(args.days))
    elif args.command == "export":
        count = export_csv(args.path)
        print(f"Exported {count} tasks to {args.path}")


if __name__ == "__main__":
    main()
