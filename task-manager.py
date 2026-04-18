tasks = []

def add_task(title):
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    print(f"Task added: {title}")

def list_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        status = "✓" if task["done"] else "✗"
        print(f"[{status}] {task['id']}. {task['title']}")

def main():
    while True:
        print("\n--- Task Manager ---")
        print("1. Add task")
        print("2. List tasks")
        print("3. Quit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Task title: ")
            add_task(title)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            break

if __name__ == "__main__":
    main()