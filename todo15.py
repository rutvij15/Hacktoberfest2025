import json
import argparse
from pathlib import Path

TASK_FILE = Path("tasks.json")

def load_tasks():
    if TASK_FILE.exists():
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {title}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📌 No tasks found!")
        return
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['title']} [{status}]")

def mark_done(index):
    tasks = load_tasks()
    try:
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print("🎉 Task marked as done!")
    except IndexError:
        print("⚠️ Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Deleted: {removed['title']}")
    except IndexError:
        print("⚠️ Invalid task number.")

parser = argparse.ArgumentParser(description="Simple To-Do CLI App")
parser.add_argument("action", choices=["add", "list", "done", "delete"])
parser.add_argument("--title", help="Task title (for add)")
parser.add_argument("--id", type=int, help="Task number (for done/delete)")

args = parser.parse_args()

if args.action == "add" and args.title:
    add_task(args.title)
elif args.action == "list":
    list_tasks()
elif args.action == "done" and args.id:
    mark_done(args.id)
elif args.action == "delete" and args.id:
    delete_task(args.id)
else:
    print("⚠️ Invalid arguments. Use --help for guidance.")
