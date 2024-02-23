#Topic 2 : MULTITHREADING (constraints of MULTITHREADING in python (GIL))
"""
summary:
In general, multi-threading means that each thread will be executed in parallel
with the other threads but this is not the case in Python because it allows only
one thread to be executed at a given time due to the existence of the GIL ( Global interpreter lock)
This Small Program demonstrates that  the time spent using multithreading is actually higher than the time spent by a single thread  for example:

Threaded : time passed =  3.422 sec
Non-threaded: time passed = 3.34 sec

Threaded > Non-threaded : Simulation for the problem that is due to the Context switching duration between the threads

"""

import threading
import time
from time import sleep
from typing import List




def myPrint(i:int)->None:
    print(f'{i}')
    for k in range(50000000):
      pass

def nonThreadedCall()->None:
    global number
    for i in range(1, number):
        myPrint(i)

def threadedCall()->None:
    allThreads = []
    global number
    for i in range(1, number):
        th = threading.Thread(target=myPrint, args=[i])
        th.start()
        allThreads.append(th)

    #our current program wait until all the threads are done
    for thread in allThreads:
        thread.join()

def calculateExecutionTime(call)->float:
    start = time.perf_counter()
    call()
    finish = time.perf_counter()
    return round(finish-start,3)

if __name__ == "__main__":
    number = int(input("-----------enter a number < a small number from 1 to 20 for example >: "))

    print(f'Threaded : time passed = {calculateExecutionTime(threadedCall)}')
    print(f'Non threaded : time passed = {calculateExecutionTime(nonThreadedCall)}')
    print('Threaded > Non-threaded : Simulation for the problem that is due to the Context switching duration between the threads')



