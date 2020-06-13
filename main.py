import task_manager as tM
import eel


eel.init('front', allowed_extensions=['.js', '.html'])

@eel.expose
def createTask(name, **params):
    tM.addTask(name, **params)
    print(f"Tache '{name}' créée avec success.")

@eel.expose
def showTasks():
    tasks = tM.getTasks()
    tasks = tasks[1:]
    for task in tasks:
        eel.addTaskElement(task)

eel.start('index.html', geometry={'size': (200, 100), 'position': (300, 50)})             # Start (this blocks and enters loop)

