import datetime
import uuid


def my_dateTime() :
    return datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")

class Task() : 

    _task_list = []
    _completed_list = []
    _incompleted_list = []

    def __init__(self, name) -> None:
        self.task = name
        self._created_time = my_dateTime()
        self._updated_time = "N/A"
        self._completed_time = "N/A"
        self._task_done = False
        self._id = str(uuid.uuid4())
        Task._task_list.append(self)
        Task._incompleted_list.append(self)

    def update_task(self, name) :
        self.task = name
        self._updated_time = my_dateTime()

    def complete_task(self): 
        self._task_done = True
        self._completed_time = my_dateTime()
        Task._completed_list.append(self)
        Task._incompleted_list.remove(self)



while True :
    print("1. Add New Task")
    print("2. Show All Tasks")
    print("3. Show Incomplete Tasks")
    print("4. Show Completed Tasks")
    print("5. Update Task")
    print("6. Mark A Task Completed")

    choice = input("Enter Option ")

    if choice == "1" :
        task_name = input("Enter New Task: ")
        Task(task_name)
        print("")
        print("Task Created Successfully")
        print("")
    elif choice == "2" :
        task_list = Task._task_list
        print("")
        if len(task_list) > 0 :
            for tsk in task_list :
                print(f"ID - {tsk._id}")
                print(f"Task - {tsk.task}")
                print(f"Created time - {tsk._created_time}")
                print(f"Updated time - {tsk._updated_time}")
                print(f"Completed - {tsk._task_done}")
                print(f"Completed time - {tsk._completed_time}")
                print("")
        else :
            print("No task created")
            print("")
    elif choice == "3" :
        incomplete_tasks = Task._incompleted_list
        print("")
        if len(incomplete_tasks) > 0 :
            for tsk in incomplete_tasks :
                print(f"ID - {tsk._id}")
                print(f"Task - {tsk.task}")
                print(f"Created time - {tsk._created_time}")
                print(f"Updated time - {tsk._updated_time}")
                print(f"Completed - {tsk._task_done}")
                print(f"Completed time - {tsk._completed_time}")
                print("")
        else :
            print("No incomplete Task")
            print("")
    elif choice == "4" :
        completed_tasks = Task._completed_list
        print("")
        if len(completed_tasks) > 0 :
            for tsk in completed_tasks :
                print(f"ID - {tsk._id}")
                print(f"Task - {tsk.task}")
                print(f"Created time - {tsk._created_time}")
                print(f"Updated time - {tsk._updated_time}")
                print(f"Completed - {tsk._task_done}")
                print(f"Completed time - {tsk._completed_time}")
                print("")
        else :
            print("No completed Task")
            print("")
    elif choice == "5" :
        task_list = [task for task in Task._task_list if task._task_done != True]
        if len(task_list) > 0 :
            print("")
            print("Select Which Task To Update")
            print("")
            for i, tsk in enumerate(task_list) :
                print(f"Task No - {i+1}")
                print(f"ID - {tsk._id}")
                print(f"Task - {tsk.task}")
                print(f"Created time - {tsk._created_time}")
                print(f"Updated time - {tsk._updated_time}")
                print(f"Completed - {tsk._task_done}")
                print(f"Completed time - {tsk._completed_time}")
                print("")
            task_num = int(input("Enter Task No: "))
            if task_num <= len(task_list) :
                new_task = input("Enter New Task ")
                print("")
                task_list[task_num-1].update_task(new_task)
                print("Task Updated Successfully")
                print("")
            else :
                if task_num <= len(task_list) :
                    print("")
                    print("Completed Task Can't Be Updated")
                    print("")
                else :
                    print("")
                    print("Invalid Task Number")
                    print("")
        else :
            print("")
            print("No Task To Update")
            print("")
    elif choice == "6" :
        task_list = Task._incompleted_list
        if len(task_list) > 0 :
            print("")
            print("Select Which Task To Complete")
            print("")
            for i, tsk in enumerate(task_list) :
                print(f"Task No - {i+1}")
                print(f"ID - {tsk._id}")
                print(f"Task - {tsk.task}")
                print(f"Created time - {tsk._created_time}")
                print(f"Updated time - {tsk._updated_time}")
                print(f"Completed - {tsk._task_done}")
                print(f"Completed time - {tsk._completed_time}")
                print("")
            task_num = int(input("Enter Task No: "))
            print("")
            if task_num <= len(task_list) and task_list[task_num-1]._task_done == False :
                task_list[task_num-1].complete_task()
                print("Task Completed Successfully")
                print("")
            else :
                print("Invalid Task Number")
                print("")
        else :
            print("")
            print("No Task To Complete")
            print("")
    else :
        print("")
        print("Please Enter A Valid Option")
        print("")

        