tasks = []

def add_task(tasks, description):
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "complete": False
    }
    tasks.append(task)  

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
        return
    for task in tasks: 
        status = "✓" if task["complete"] else "✗"
        print(f"[{status}] {task['id']}. {task['description']}")

def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["complete"] = True
            print(f"Task {task_id} marked as complete.")
            return
        print(f"Task {task_id} not found.")
    
   
def delete_task(tasks, task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            print(f"Task {task_id} deleted.")
            return
    print(f"Task {task_id} not found.")

def save_tasks(tasks, filename):
    with open(filename, "w") as f:
        for task in tasks:
            complete = "1" if task["complete"] else "0"
            f.write(f"{task['id']}|{task['description']}|{complete}\n")
    print("Tasks saved.")

def load_tasks(filename):
    tasks = []
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                tasks.append({
                    "id": int(parts[0]),
                    "description": parts[1],
                    "complete": parts[2] == "1"
                })
    except FileNotFoundError:
        pass
    return tasks

def main():
    tasks = load_tasks("tasks.txt")
    print("Welcome to Fleet To-Do CLI")
    while True:
        print("\n1. Add task\n2. View tasks\n3. Complete task\n4. Delete task\n5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            desc = input("Task description: ")
            add_task(tasks, desc)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            task_id = int(input("Task ID to complete: "))
            complete_task(tasks, task_id)
        elif choice == "4":
            task_id = int(input("Task ID to delete: "))
            delete_task(tasks, task_id)
        elif choice == "5":
            save_tasks(tasks, "tasks.txt")
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
