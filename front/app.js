eel.expose(addTaskTable); 

function addTaskTable(task) {
    li = document.createElement("li");
    li.innerHTML = task["name"];
    li.classList.add("task")
    document.getElementById("TaskList").appendChild(li)
}

eel.showTasks();

let input = document.getElementById("task_name")
document.getElementById("new_task").addEventListener("click", function (e){
    e.preventDefault;
    let taskName = input.value
    console.log(taskName);
    eel.createTask(taskName)
    input.value = ""

    li = document.createElement("li");
    li.innerHTML = taskName;
    li.classList.add("task")
    document.getElementById("TaskList").appendChild(li)
    return false;
})