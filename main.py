import os, sys, subprocess

def createTask(name, options = None):
    command = "task add '" + name + "' "
    if not options:
        pass
    else:    
        for option in options.keys():
            command += option + ":" + options[option]

    os.system(command)

def deleteTask(id):
    command = "task " + str(id) + " delete"
    os.system(command)

def getTasks():
    with open("tasks.txt", "w") as file:
        file.write('') #Supression du contenu

    command = "task > tasks.txt"

    os.system(command)

    with open('tasks.txt', 'r') as file:
        tasks = file.read()
    print(tasks)