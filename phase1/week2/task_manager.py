# I am building a TaskManager class.
# It will store tasks in self.tasks
# It will have these methods:
# - add_task
# - view_tasks
# - complete_task
# - delete_task
# - save_tasks
# - load_tasks

class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, description):
        task = {
            "id": len(self.tasks)+1,
            "description": description,
            "complete": False
        }
        self.tasks.append(task)
    def view_tasks(self):
        if len(self.tasks) ==0:
            print("No tasks yet.")
            return
        for task in self.tasks:
            status = "✓" if task["complete"] else "✗"
            print(f"[{status}] {task['id']}. {task['description']}")
            
    def complete_task(self, task_id):
        for task in self.tasks:
            if task ["id"] == task_id:
                task["complete"] = True
                print(f"task {task_id} marked as complete.")
                return
            
        print(f"Task {task_id} not found.")
    def delete_task(self, task_id):
        for i in range(len(self.tasks)):
            if self.tasks[i]['id'] == task_id:
                self.tasks.pop(i)
                print(f"Task {task_id} deleted.")
                return
    def save_tasks(self, filename):
        with open (filename, "w") as f:
            for task in self.tasks:
                complete = "1" if task ["complete"] else "0"
                f.write(f"{task['id']}|{task['description']}|{complete}\n")
            print("Tasks saved.")
    def load_tasks(self, filename):
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
            print("File not found.")
        self.tasks = tasks
        pass

    def main(self):
        self.load_tasks("tasks.txt")
        print("Welcome to Fleet To-Do CLI")
        while True:
            print("\n1. Add task\n2. View tasks\n3. Complete task\n4. Delete task\n5. Exit")
            choice = input("Choose: ").strip()
            if choice == "1":
                desc = input ("Task description: ")
                self.add_task(desc)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                task_id = int(input("Enter task id to complete: "))
                self.complete_task(task_id)
            elif choice == "4":
                task_id = int(input("Enter task id to delete: "))
                self.delete_task(task_id)
            elif choice == "5":
                self.save_tasks("tasks.txt")
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = TaskManager()
    manager.main()    