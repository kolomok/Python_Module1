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
            f.write(f"{taskid} | {task['Название']} | {task['Описание']} | {task['Приоритет']} | {task['Статус']} \n")

def createtask(tasks):
    title = input("Введите название задачи: ")
    description = input("Введите описание задачи: ") 
    
    while True: 
        priority = input("Задайте приоритет задаче:")
        if priority in prioties:
            break 
        print("Ошибка! Введите правильное значение: ")

    while True: 
        status = input("Задайте статус задаче: ")
        if status in statuses: 
            break 
        print("Ошибка! Введите правильное значение: ")
    taskid = tasknextid(tasks)
    tasks[taskid] = {"Название": title,
                 "Описание": description,
                 "Статус": statuses[status],
                 "Приоритет": prioties[priority]
    }

    save(tasks)
    print(f"Задача с ID {taskid} создана!")
    
def disp(tasks):
    if not tasks:
        print('Нет задач')
        return
    
    print('\n Список задач:')
    for taskid, task in tasks.item():
        print (f"[{taskid}] {task['Название']} | {task['Приоритет']} | {task['Статус']}")

def delete(tasks):
    taskid = input('Введите ID задачт для удаления: ')
    if taskid in tasks:
        del tasks[taskid]
        save(tasks)
        print("Задача удалена")
    else:
        print("Задача не найдега")
