class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{status} {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task '{description}' added.")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print(f"Task '{self.tasks[index].description}' marked as completed.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")
        else:
            print("No tasks in the list.")

# Example usage:
if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List Manager =====")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
