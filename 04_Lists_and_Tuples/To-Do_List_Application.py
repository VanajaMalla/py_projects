# Descrption: 

# This To-do list application project is based on python concepts : Lists and tuples

# Tasks are stored as tuples in a list: (task_name, is_done)



def display_task(tasks):
    if not tasks:
        print("To do list is empty.")
    else:
        for i,(task,done) in enumerate(tasks,start = 1):
            status = "✔" if done else "✘"
            print(f"{i}.{task} [{status}]")           

def add_task(tasks):
    task = input("Enter Task:").strip()
    if task:
        tasks.append((task,False))
        print("Task added successfully.")
    else:
        print("Empty task can't be added.")
                 
def mark_done(tasks):
    nth_task = int(input("Enter the number of task that to be marked as done: "))
    if 1<=nth_task<=len(tasks):
        (task,_) = tasks[nth_task-1]
        tasks[nth_task-1] =(task, True)
        print("Marked as done.")
    else:
        print("Invalid task number. ")

def delete_task(tasks):
    nth_task = int(input("Enter the number of task that to be deleted: "))
    if 1<=nth_task<=len(tasks):
        tasks.pop(nth_task-1)
        print("Task has been deleted.")
    else:
        print("Invalid task number. ")

if __name__ == "__main__" :  
    
    tasks = [] 
    
    while True:
        
        print("To-Do List Menu:")
        print("1. Display tasks")
        print("2. Add new task")
        print("3. Mark as Done")
        print("4. Delete task")
        print("5. Exit")
        
        choice = int(input("Enter your choice :"))
        
        
        if choice == 1:
            display_task(tasks)
        elif choice == 2:
            add_task(tasks)
        elif choice == 3:
            mark_done(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            print("Thank You. Good Bye.")
            break
        else:
            print("Invalid Input")
