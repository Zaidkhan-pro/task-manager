tasks = []

def add_task(title, priority="normal"):              # ← CHANGED
    task = {"id": len(tasks) + 1, "title": title, "done": False, "priority": priority}
    tasks.append(task)
    print(f"Task added: {title} [{priority}]")

def list_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        status = "✓" if task["done"] else "✗"
        print(f"[{status}] {task['id']}. {task['title']} [{task['priority']}]")

def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            print(f"Task {task_id} marked as complete.")
            return
    print("Task not found.")

def main():
    while True:
        print("\n--- Task Manager ---")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete a task")
        print("4. Quit")                             # ← still 4, no delete here
        choice = input("Choose: ")

        if choice == "1":
            title = input("Task title: ")
            priority = input("Priority (low/normal/high): ")   # ← NEW
            add_task(title, priority)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_id = int(input("Task ID to complete: "))
            complete_task(task_id)
        elif choice == "4":
            break

if __name__ == "__main__":
    main()