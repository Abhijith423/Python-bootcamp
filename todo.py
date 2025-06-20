todo_list = []

def show_tasks():
    if not todo_list:
        print("\n📭 No tasks in your list.")
    else:
        print("\n📋 Your Tasks:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def add_task():
    task = input("➕ Enter the task: ").strip()
    if task:
        todo_list.append(task)
        print("✅ Task added.")
    else:
        print("⚠️ Task cannot be empty!")

def remove_task():
    show_tasks()
    if todo_list:
        try:
            index = int(input("❌ Enter task number to remove: "))
            if 1 <= index <= len(todo_list):
                removed = todo_list.pop(index - 1)
                print(f"✅ Removed task: {removed}")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

def main():
    while True:
        print("\n====== To-Do List Menu ======")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("👋 Exiting. Have a niceday!")
            break
        else:
            print("❗ Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
