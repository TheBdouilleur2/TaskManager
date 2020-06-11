import json

def getTasks(**param):
    tasks = []

    with open("tasks.json") as file:
        fileContent = json.load(file)

    for task in fileContent:
        if param:
            for critere in param.keys():
                if critere in task.keys():
                    if param[critere] == task[critere]:
                        tasks.append(task)

        else:
            tasks.append(task)

    return tasks

def getTask(ID):
    tasks = []

    tasks = getTasks()

    return tasks[ID]

def writeTasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file,  indent=4)

def getLastID():
    with open("tasks.json") as file:
        fileContent = json.load(file)

    lastID = fileContent[0]["lastID"]
    return lastID
    

#Ajoute une tache dans le fichier json
#@param params un dictionnaire contenant les parametres #à passer.
def addTask(name, **params):
    lastID = getLastID()
    task = {"ID": lastID + 1, "name":name}
    if params:
        for name in params.keys():
            task[name] = params[name]
    tasks = getTasks()
    tasks.append(task)
    tasks[0]["lastID"] += 1
    writeTasks(tasks)

def addParams(ID, **params):
    task = getTask(ID) 
    if params:
        for name in params.keys():
            task[name] = params[name]
    tasks = getTasks()
    tasks[ID] = task
    writeTasks(tasks)

def deleteTask(ID):
    tasks = getTasks()
    if ID < len(tasks):
        del tasks[ID]
    else:
        print("La tache n'existe pas!")
        return False
    i = 0
    for task in tasks:
        task['ID'] = i
        i += 1
    tasks[0]["lastID"] -= 1
    writeTasks(tasks)


