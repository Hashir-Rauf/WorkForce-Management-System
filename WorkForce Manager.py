robots = {}
workers = {}
tasks = []
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
#def createTask(): 
#def assignTask():
#def completeTask():
#def checkStatus():
#def addProduct():
#def assignProduct():

while True:
    print("Enter your desired operation\n1: Add a Robot \n2: Remove a Robot")
    print("3: Add a Worker\n4: Remove a Worker\n5: View Current Workforce\n")
    UserInput = input("Enter \"exit\" to exit the program:\t")
    print("\n")
    if UserInput.lower() == "exit":
        break
    match UserInput:
        case "1":
            addRobot(robots,int(input("Enter the Robot's ID: ")))
            print("\n")
        case "2":
            removeRobot(robots,int(input("Enter the Robot's ID: ")))
            print("\n")
        case "3":
            addWorker(workers,int(input("Enter the Worker's ID: ")))
            print("\n")
        case "4":
            removeWorker(workers,int(input("Enter the Worker's ID: ")))
            print("\n")
        case "5":
            viewWorkForce(workers,robots)
            print("\n")
        case _:
            print("Invalid Operation")