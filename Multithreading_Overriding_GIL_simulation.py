#Topic 4 : multithreaded program that overrides the GIL (using the sleep function)
"""
summary:
In the following program, we use the function sleep which overrides the GIL thus the threads can be executed simultaneously( in parallel)
In this example the time spent by the multi-threaded version of this program will be less than the version using a single thread :

for example:
Threaded: time passed = 1.01
Non-threaded: time passed = 3.019


"""

import threading
import time
from time import sleep
from typing import List

def myPrint(i:int)->None:
    print(f'{i}')
    time.sleep(1)

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

if __name__ == '__main__':
    number = int(input("enter a number < a small number from 1 to 20 for example >: "))

    print(f'Threaded : time passed = {calculateExecutionTime(threadedCall)}')
    print(f'Non threaded : time passed = {calculateExecutionTime(nonThreadedCall)}')
    input()


