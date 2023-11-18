# TASK 1 - TO-DO LIST

#Defining a dictinory where we store the task and thier status
Tasks ={}

# Defining Functions
# Function to add a task
def Add_Task(Task,Status="TO DO"):
    Tasks[Task]=Status
    print(f"Task '{Task}' is added to the TO-DO List!")

# Function to Display(List) the tasks
def List_Tasks():
    if Tasks:
        print("TO-DO List:-")
        for Task,Status in Tasks.items():
            print(f"{Task}-Status:{status}")
    else:
        print("Your TO-DO List is Empty!")

# Function to Update the Task Status
def Update_Task_Status(Task,Status):
    if Task in Tasks:
        Tasks[Task]=Status
        print(f"Task '{Task}' Status updated to '{Status}'.")
    else:
     print(f"Task '{Task}' not found in the TO-DO List.")

# Function to Remove a Task
def Remove_Task(Task):
    if Task in Tasks:
        del Tasks[Task]
        print(f"Task '{Task}' removed from the TO-DO List.")
    else:
     print(f"Task '{Task}' not found in the TO-DO List.")

# Main Loop
while True:
    command=input("Enter a command (add,list,update,remove,quit):").lower()

    if command == "add":
        Task=input("Ente the Task:")
        Add_Task(Task)
    elif command== "list":
        List_Tasks()
    elif command == "update":
        Task = input("Enter the Task to update:")
        Status = input("Enter the New Status:")
        Update_Task_Status(Task,Status)
    elif command == "remove":
        Task = input("Enter the Task you want to Remove:")
        Remove_Task(Task)
    elif command == "quit":
        print("Goodbye!")
        break
    else:
        print("INVALID COMMAND")
        print("PLEASE USE THE add,list,update,remove,quit COMMANDS!")
        









    
    





    
