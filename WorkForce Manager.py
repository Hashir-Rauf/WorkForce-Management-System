robots = {} #Robots Dictionary to hold robots data
workers = {} #workers Dictionary to hold workers data
tasks = {} #tasks Dictionary to hold tasks data
products = {} #products dictionary to hold products data
task_queue = [] #tasks queue to wait until resources are free

def addRobot(robots, Id): #Function to add robots with unique ID
    if Id in robots.keys(): #Checking Uniqueness
        print(f"Robot with ID: {Id} already exists")
    else:
        robots[Id] = {"status": "idle"} #Adding robot with given ID and its status set to Idle
        print(f"Robot {Id} added")

def removeRobot(robots, Id): #Function to remove robots
    if Id in robots.keys() and robots[Id]["status"] == "idle": #Check for existence of the robot and is idle
        del robots[Id]
        print(f"Robot {Id} removed")
    else: #the robot does not exist
        print(f"No Robot with ID: {Id} exists or is Busy")

def addWorker(workers, Id): #same as add robot but for workers
    if Id in workers.keys():
        print(f"Worker with ID: {Id} already exists")
    else:
        workers[Id] = {"status": "idle"}
        print(f"Worker {Id} added")

def removeWorker(workers, Id): #same as remove robot but for workers
    if Id in workers.keys() and workers[Id]["status"] == "idle":
        del workers[Id]
        print(f"Worker {Id} removed")
    else:
        print(f"No Worker with ID: {Id} exists")

def viewWorkForce(workers, robots): #Method to print total workforce and their status
    print("Workers\t\tStatus\n")
    for i in workers.keys():
        print(f"Worker {i}\t{workers[i]['status']}")
    print("\nRobots\t\tStatus\n")
    for i in robots.keys():
        print(f"Robot {i}\t{robots[i]['status']}")

def createTask(taskID, taskName, taskWorkersReq, taskRobotsReq): #Method to create a task
    if len(robots) < taskRobotsReq or len(workers) < taskWorkersReq: # checking if we have enough resources
        print("Not enough Resources")
        return
    if taskID in tasks.keys(): #checking for uniqueness
        print(f"Task with ID {taskID} already exists")
    else:
        tasks[taskID] = [taskName, taskWorkersReq, taskRobotsReq, "Not Started"]
        print(f"Task {taskID} created")

def assignTask(taskID): #method to assign a task to available workforce
    IdleWorkers = [i for i in workers if workers[i]["status"] == "idle"] #fetching all idle workers
    IdleRobots = [i for i in robots if robots[i]["status"] == "idle"] #feteching all idle robots

    if taskID not in tasks.keys(): #checking for task availability
        print(f"Task with ID {taskID} does not exist")
        return

    if len(IdleWorkers) >= tasks[taskID][1] and len(IdleRobots) >= tasks[taskID][2]: #checking whether we have enough idle resources
        for i in IdleWorkers[:tasks[taskID][1]]: #updating the workers  status
            workers[i]["status"] = "working"
            workers[i]["Current Task"] = taskID
        for i in IdleRobots[:tasks[taskID][2]]: #updating the robots status
            robots[i]["status"] = "working"
            robots[i]["Current Task"] = taskID
        tasks[taskID][3] = "Started" #updating the task status
        print(f"Task {taskID} has been started.")
    else:
        print("Not enough resources available. Adding task to queue.")
        task_queue.append(taskID) #adding to the queue for  when resources  are available

def checkQueue():
    global task_queue #global varaible of tasks queue
    if not task_queue: #if it doesn't exists
        return
    for taskID in task_queue[:]: 
        IdleWorkers = [i for i in workers if workers[i]["status"] == "idle"]
        IdleRobots = [i for i in robots if robots[i]["status"] == "idle"]
        if len(IdleWorkers) >= tasks[taskID][1] and len(IdleRobots) >= tasks[taskID][2]:
            assignTask(taskID) #assigning the task
            task_queue.remove(taskID) #removing from queue

def checkStatus(): #to monitor all current workforce and
    print("Task Status:\n")
    for taskID, taskDetails in tasks.items(): #Printing all current tasks in the system
        print(f"Task {taskID} - {taskDetails[3]}")
    print("\nWorker Status:\n") #printing all workers in the system
    for workerID, details in workers.items():
        print(f"Worker {workerID} - {details['status']}")
    print("\nRobot Status:\n") #printing all robots in the system
    for robotID, details in robots.items():
        print(f"Robot {robotID} - {details['status']}")
    print("\nProduct Status:\n") #printing all product information in the system
    for productID, details in products.items():
        print(f"Product {productID}:")
        for stepName, stepDetails in details["steps"].items():
            taskID, taskName, workersRequired, robotsRequired = stepDetails
            stepStatus = tasks[taskID][3] if taskID in tasks else "Task not created"
            print(f"  Step: {stepName}")
            print(f"    Task ID: {taskID}")
            print(f"    Task Name: {taskName}")
            print(f"    Workers Required: {workersRequired}")
            print(f"    Robots Required: {robotsRequired}")
            print(f"    Status: {stepStatus}")

def completeTask(taskID): #to complete a task
    if taskID in tasks.keys() and tasks[taskID][3] == "Started": #checking if  a task is started or not and does it exist or not
        for workerID in workers.keys():
            if workers[workerID].get("Current Task") == taskID: #accesing all the workers with assignment to this task
                workers[workerID]["status"] = "idle" #Setting the status of workers as idle once the task is complete
                del workers[workerID]["Current Task"] #removing their current task data
        for robotID in robots.keys():
            if robots[robotID].get("Current Task") == taskID:  #accesing all the robots with assignment to this task
                robots[robotID]["status"] = "idle" #Updating their status to idle once task is complete
                del robots[robotID]["Current Task"] #removing their current task data
        tasks[taskID][3] = "Completed" #setting the task status to complete
        print(f"Task {taskID} has been completed.")
        checkQueue() #checking if the queue is empty or not
    else:
        print(f"Task {taskID} is not started or does not exist.") #if the task does not exist or hasn't been started

def addProduct(productID, steps):
    if productID in products.keys():# Check if the product ID already exists
        print(f"Product with ID {productID} already exists")
    else:
        product_steps = {}  # Initialize a dictionary to store steps for the product
        for step in steps:
            taskID = f"{productID}_{step}"    # Generate a unique task ID for each product step
            taskName = input(f"Enter Task Name for step '{step}': ")  # Prompt user for task details for the current step
            workersRequired = int(input(f"Enter Workers Required for step '{step}': "))
            robotsRequired = int(input(f"Enter Robots Required for step '{step}': "))
            createTask(taskID, taskName, workersRequired, robotsRequired)# Create the task with the provided details
            product_steps[step] = [taskID, taskName, workersRequired, robotsRequired] # Store the task details in the product_steps dictionary
        products[productID] = {"steps": product_steps} # Store the task details in the product_steps dictionary
        print(f"Product {productID} added with steps: {product_steps}")

for i in range(10):# Prepopulate the workers dictionary with 10 idle workers
    addWorker(workers, str(i + 1))

for i in range(5): # Prepopulate the robots dictionary with 5 idle robots
    addRobot(robots, str(i + 1))


while True: # Infinite loop for user interaction until the user exits
    # Display menu options for the user
    print("\nEnter your desired operation")
    print("1: Add a Robot\n2: Remove a Robot")
    print("3: Add a Worker\n4: Remove a Worker")
    print("5: View Current Workforce\n6: Create Task\n7: Assign Task")
    print("8: Check Status\n9: Complete Task\n10: Add Product")
    UserInput = input("Enter 'exit' to exit the program: ")
    if UserInput.lower() == "exit": # Exit condition for breaking the loop
        break
    match UserInput:# Match user input with operations
        case "1":
            addRobot(robots, input("Enter the Robot's ID: "))  # Add a new robot
        case "2":
            removeRobot(robots, input("Enter the Robot's ID: "))  # Remove a robot
        case "3":
            addWorker(workers, input("Enter the Worker's ID: "))  # Add a new worker
        case "4":
            removeWorker(workers, input("Enter the Worker's ID: "))  # Remove a worker
        case "5":
            viewWorkForce(workers, robots)  # View the current workforce
        case "6":
            taskID = input("Enter Task ID: ") # Create a new task
            createTask( taskID,input("Enter Task Title: "),int(input("Enter Workers Requirement: ")),int(input("Enter Robots Requirement: ")))
        case "7":
            assignTask(input("Enter Task ID: "))  # Assign a task to available resources
        case "8":
            checkStatus()  # Check the status of tasks, workers, and robots
        case "9":
            completeTask(input("Enter the Task ID to complete: "))  # Complete a task
        case "10":
            productID = input("Enter Product ID: ")            # Add a new product with multiple steps
            steps = input("Enter steps (comma-separated): ").split(",")
            addProduct(productID, steps)
        case _:
            print("Invalid Operation")  # Handle invalid input
