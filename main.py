file = "tasks.txt"
statuses = {1:"Новая", 2:"В процессе", 3:"Завершена"}
prioties = {1:"Низкий", 2:"Средний", 3:"Высокий"} 

def open_tasks():
    tasks = {}
    with open(file, "r") as f:
        for line in f:
            part = line.strip().split("|")
            if len(part) == 5:
                taskid, title, description, priority, status = part
                tasks[taskid] = {'Название': title,
                         'Описание': description,
                         'Приоритет': priority,
                         'Статус': status}
    return tasks            

def tasknextid(taskid):
    if not tasks:
        return "1"
    return str(max(map(int, tasks.key))) + 1

def save(tasks):
    with open(file, "w") as f:
        for taskid, task in tasks.item():
            f.write(f"{taskid} | {task['Название']} | {task['Описание']} | {task['Приоритет']} | {task['Статус']}")