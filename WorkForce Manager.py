robots = {}
workers = {}
tasks = {}
products = {}
def addRobot(robots,Id):
    if Id in robots.keys():
        print(f"Robot with ID:{Id} Already Exists")
    else:
        robots[Id] = {"status": "idle"}
    return robots
def removeRobot(robots , Id):
    if Id in robots.keys():
        del robots[Id]
    else:
        print(f"No Robot with ID: {Id} exists")
def addWorker(workers,Id):
    if Id in workers.keys():
        print(f"Worker with ID:{Id} Already Exists")
    else:
        workers[Id] = {"status": "idle"}
    return workers
def removeWorker(workers , Id):
    if Id in workers.keys():
        del workers[Id]
    else:
        print(f"No Worker with Id: {Id} exists")
def viewWorkForce(workers,robots):
    print( "Workers\n")
    for i in workers.keys():
        print(f"Worker: {i}")
    print("\nRobots\n")
    for i in robots.keys():
        print(f"Robot: {i}")
def createTask(taskID , taskName , taskWorkersReq , taskRobotsReq):
   if taskID in tasks.keys():
       print(f"Task with ID {taskID} already exists")
   else:
       tasks[taskID] = [taskName , taskWorkersReq , taskRobotsReq , "Not Started"]


def assignTask(taskID):
    IdleWorkers = []
    IdleRobots  = []
    for i in workers.keys():
        if workers[i]["status"] == "idle":
            IdleWorkers.append(i)
    for i in robots.keys():
        if robots[i]["status"] == "idle":
            IdleRobots.append(i)
    if taskID not in tasks.keys():
        print(f"task with ID {taskID} does not exist")
        return
        
    if len(IdleRobots) >= tasks[taskID][2] and len(IdleWorkers) >= tasks[taskID][1]:
        for i in IdleRobots[:tasks[taskID][2]]:
            robots[i]["status"] = "working"
            robots[i]["Current Task"] = taskID
        for i in IdleWorkers[:tasks[taskID][1]]:
            workers[i]["status"] = "working"
            workers[i]["Current Task"] = taskID
        tasks[taskID][3] = "Started"
        print(f"Task {taskID} has been started.")
    else:
        print("Not Enough Resources Available")
                              
def checkStatus():
    print("Task Status:\n")
    for taskID , taskDetails in tasks.items():
        print(f"Task{taskID} - {taskDetails[3]}")
    print("\nWorker Status:\n")
    for workerID, details in workers.items():
        print(f"Worker {workerID} - {details['status']}")
    print("\nRobot Status:\n")
    for robotId , details in robots.items():
        print(f"Robots {robotId} - {details['status']}")
    
def completeTask(taskID):
    if taskID in tasks.keys() and tasks[taskID][3] == "Started":
        for workerID in workers.keys():
            if workers[workerID].get("Current Task") == taskID:
                workers[workerID]["status"] = "idle"
                del workers[workerID]["Current Task"]
        for robotID in robots.keys():
            if robots[robotID].get("Current Task") == taskID:
                robots[robotID]["status"] = "idle"
                del robots[robotID]["Current Task"]
        tasks[taskID][3] = "Completed"
        print(f"Task {taskID} has been completed.")
    else:
        print(f"Task {taskID} is not started or does not exist.")

def addProduct(productID, steps):
    if productID in products.keys():
        print(f"Product with ID {productID} already exists")
    else:
        products[productID] = steps
        print(f"Product {productID} added with steps: {steps}")

while True:
    print("\nEnter your desired operation")
    print("1: Add a Robot\n2: Remove a Robot")
    print("3: Add a Worker\n4: Remove a Worker")
    print("5: View Current Workforce\n6: Assign Task")
    print("7: Check Status\n8: Complete Task\n9: Add Product")
    UserInput = input("Enter 'exit' to exit the program: ")

    if UserInput.lower() == "exit":
        break

    match UserInput:
        case "1":
            addRobot(robots, int(input("Enter the Robot's ID: ")))
        case "2":
            removeRobot(robots, int(input("Enter the Robot's ID: ")))
        case "3":
            addWorker(workers, int(input("Enter the Worker's ID: ")))
        case "4":
            removeWorker(workers, int(input("Enter the Worker's ID: ")))
        case "5":
            viewWorkForce(workers, robots)
        case "6":
            taskID = input("Enter task ID: ")
            createTask(taskID, input("Enter Task Title: "), int(input("Enter Workers Requirement: ")), int(input("Enter Robots Requirement: ")))
            assignTask(taskID)
        case "7":
            checkStatus()
        case "8":
            completeTask(input("Enter the Task ID to complete: "))
        case "9":
            productID = input("Enter Product ID: ")
            steps = input("Enter steps (comma-separated): ").split(",")
            addProduct(productID, steps)
        case _:
            print("Invalid Operation")
