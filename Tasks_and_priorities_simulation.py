# Topic 1 : TASKS and PRIORITIES
"""
summary:
 in this section we have a small program that demonstrates how a single thread manages priorities
 how it works:  the user assigns a priority(1,2…etc) To each of the tasks  A,B ,C so that the thread
 executes these tasks in the desired order(tasks having smaller priority value starts first)
"""
import threading
import time
from time import sleep
from typing import List



def jobA(priority:int):
    print(f'Task -A- is executing (priority= {priority})')
    sleep(1)

def jobB(priority:int):
    print(f'Task -B- is executing (priority= {priority})')
    sleep(1)

def jobC(priority:int):
    print(f'Task -C- is executing (priority= {priority})')
    sleep(1)

class Task:
    def __init__(self,job,priority):
        self.__job = job
        self.priority = priority

    def DoJob(self):
        self.__job(self.priority)


def execute(allTasks :List[Task]):
    allTasks.sort(key=lambda task : task.priority)
    while len(allTasks) != 0:
        allTasks[0].DoJob()
        allTasks.pop(0)

    print("Done")



if __name__ == "__main__":
    print("########################## TASKS and PRIORITIES ####################################")
    pA = int(input("Priority of Task -A- : "))
    pB = int(input("Priority of Task -B- : "))
    pC = int(input("Priority of Task -C- : "))

    tA = Task(job=jobA,priority=pA)
    tB = Task(job=jobB,priority=pB)
    tC = Task(job=jobC,priority=pC)

    allTasks = [tA,tB,tC]
    thread = threading.Thread(target=execute,args=[allTasks])
    thread.start()
    thread.join()

    input()

