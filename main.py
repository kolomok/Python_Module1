filename = "tasks.txt"
statuses = {1:"Новая", 2:"В процессе", 3:"Завершена"}
prioties = {1:"Низкий", 2:"Средний", 3:"Высокий"} 

def open_tasks():
    tasks = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                part = line.strip().split("|")
                if len(part) == 5:
                    taskid, title, description, priority, status = part
                    taskid = int(taskid)
                    tasks[taskid] = {'Название': title,
                            'Описание': description,
                             'Приоритет': priority,
                            'Статус': status}
    except FileNotFoundError:
        return{}
    return tasks            

def tasknextid(tasks):
    if not tasks:
        return 1
    return max(map(int, tasks.keys())) + 1

def save(tasks):
    with open(filename, "w", encoding="utf-8") as f:
        for taskid, task in tasks.items():
            filename.write(f"{taskid} | {task['Название']} | {task['Описание']} | {task['Приоритет']} | {task['Статус']} \n")

def createtask(tasks):
    title = input("Введите название задачи: ")
    description = input("Введите описание задачи: ") 
    
    while True: 
        priority = int(input("Задайте приоритет задаче:"))
        if priority in prioties:
            break 
        print("Ошибка! Введите правильное значение: ")

    while True: 
        status = int(input("Задайте статус задаче: "))
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
    for taskid, task in tasks.items():
        print (f"[{taskid}] {task['Название']} | {task['Приоритет']} | {task['Статус']}")

def delete(tasks):
    try:
        taskid = int(input('Введите ID задачи для удаления: '))
    except ValueError:
        print("Ошибка! Введите число.")
        return

    if taskid in tasks:
        del tasks[taskid]
        save(tasks)
        print(f"Задача {taskid} удалена")
    else:
        print("Задача не найдена")

def update(tasks):
    try:
        taskid = int(input('Введите ID задачи для изменения: '))
    except ValueError:
        print("Ошибка! Введите число.")
        return

    if taskid not in tasks:
        print("Задача не найдена")
        return

    print('Что хотите изменить?')
    print('1 - Название задачи\n2 - Описание задачи\n3 - Статус задачи\n4 - Приоритет задачи')

    try:
        choice = int(input("Введите число: "))
    except ValueError:
        print("Ошибка! Введите число от 1 до 4.")
        return

    if choice == 1:
        tasks[taskid]["Название"] = input("Введите новое название задачи: ")
    elif choice == 2:
        tasks[taskid]["Описание"] = input('Введите новое описание задачи: ')
    elif choice == 3:
        while True:
            try:
                status = int(input('Выберите статус (1 - новая, 2 - в процессе, 3 - завершена): '))
                if status in statuses:
                    tasks[taskid]['Статус'] = statuses[status]
                    break
                print('Неверный ввод! Повторите попытку.')
            except ValueError:
                print('Ошибка! Введите число от 1 до 3.')
    elif choice == 4:
        while True:
            try:
                priority = int(input("Выберите приоритет (1 - низкий, 2 - средний, 3 - высокий): "))
                if priority in prioties:
                    tasks[taskid]['Приоритет'] = prioties[priority]
                    break
                print("Неверный ввод! Повторите попытку.")
            except ValueError:
                print('Ошибка! Введите число от 1 до 3.')
    else:
        print('Неверный ввод!')

    save(tasks)
    print(f"Задача {taskid} обновлена")

def main():
    tasks = open_tasks()

    if tasks is None:  
        tasks = {} 

    while True:
        print("Меню: \n1 - Создать задачу \n2 - Просмотреть задачи \n3 - Обновить задачу \n4 - Удалить задачу \n0 - Выйти")

        try:
            choice = int(input("Введите число: "))  
        except ValueError:
            print("Ошибка! Введите число от 0 до 4.")
            continue  

        if choice == 1:
            createtask(tasks)
        elif choice == 2:
            disp(tasks)
        elif choice == 3:
            update(tasks)
        elif choice == 4:
            delete(tasks)
        elif choice == 0:
            break
        else:
            print("Error!!!")

if __name__ == "__main__":
    main()