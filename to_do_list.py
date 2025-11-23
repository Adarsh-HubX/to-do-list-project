# Project Title : Simple To-Do List (Python)
# Name          : Adarsh Rathore
# Course        : B.Tech CSE (Cyber Security)
# Roll Number   : 2501410014
# Faculty       : Dr. Feroz Ahmad Sir
# Date          : 23 Nov 2025


#Simple to-do-lists-project

todo_list = []

def menu():
    print("\n----- TO DO LIST -----")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Mark task as done")
    print("5. Exit")

def add_task():
    t = input("Enter task: ")
    if t.split() == "":
        print("Task cannot be empty.")
        return
    todo_list.append({"name": t, "done": False})
    print("Task added.")

def view_task():
    print("\nYour tasks:")
    if len(todo_list) == 0:
        print("No tasks added yet.")
    else:
        for i, item in enumerate(todo_list):
            status = "Done" if item["done"] else "Not done"
            print(f"{i+1}. {item['name']} - {status}")

def delete_task():
    view_task()
    num = input("Task number to delete: ")
    if num.isdigit():
        i = int(num) - 1
        if 0 <= i < len(todo_list):
            removed = todo_list.pop(i)
            print(f"Removed: {removed['name']}")
        else:
            print("Invalid number.")
    else:
        print("Enter a valid number.")

def mark_done():
    view_task()
    num = input("Task number to mark done: ")
    if num.isdigit():
        i = int(num) - 1
        if 0 <= i < len(todo_list):
            todo_list[i]["done"] = True
            print("Task marked done.")
        else:
            print("Invalid number.")
    else:
        print("Enter a valid number.")

while True:
    menu()
    # user option input
    ch = input("Choose option: ")

    if ch == "1":
        add_task()
    elif ch == "2":
        view_task()
    elif ch == "3":
        delete_task()
    elif ch == "4":
        mark_done()
    elif ch == "5":
        print("Exit...")
        break
    else:
        print("Invalid choice.")
