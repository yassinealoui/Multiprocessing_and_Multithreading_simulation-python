

import threading
import time
from time import sleep
from typing import List
"""
hello miss our work is divided into 5 sections,to see each section just uncoment that section then recoment it to see other sections

Section1 : TASKS and PRIORITIES
Section 2 : MULTITHREADING (constraints of MULTITHREADING in python (GIL))
#Section3 : simulation that demonstrates how the GIL works
#section 4 : multithreaded program that overrides the GIL (using the sleep function)
#section5 : multiprocessing

"""










#section5 : multiprocessing
"""
summary :
Because multithreading doesn't work exactly as we want it in Python we used the concept of multiprocessing which
is creating multiple processes each of them executes a different task

This small Program is created To visually demonstrate how single process execute its tasks and also to visually 
demonstrate how multiple processes execute these tasks in parallel ,if you execute this program you will be prompted 
by a window  that is named with the PID(process ID)  of the current process ,in this window you will see 
four rectangles( having different colors) that are being constructed ,  those rectangles represents the tasks that 
our  process is currently executing, as you will see those tasks are being completed one after the other

Now if you comment the line : 
singleThread_singleProcess() —-> #singleThread_singleProcess()

and uncomment the other line : 
#multiProcessingCall() ---> multiProcessingCall()

our program will create four processes each of them having its PID number And each of them will start doing 
a specific task, these processes will be executing simultaneously as you will see four windows that will pop up each 
of them is constructing  a rectangle with a specific color representing  specific task.


"""
import os
import sys
from multiprocessing import Process,cpu_count
import pygame
import numpy as np

colors =  [(50,205,50),(64,224,208),(75,0,130),(139,69,19),(112,128,144),(255,69,0),(169,169,169)]
def getNextColor(color):
    ind = colors.index(color)
    return colors[ind +1] if ind +1 < len(colors) else colors[0]

def setWindowsPosition(x,y):
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)





class Window():
    def __init__(self,xDimension,yDimension,ProcessOrder=0,taskOrder=None):
        self.xDimension = xDimension
        self.yDimension = yDimension
        self.ProcessOrder = ProcessOrder
        self.taskOrder = taskOrder

    def createwindow(self):
        self.screen = pygame.display.set_mode((self.xDimension, self.yDimension))
        caption = f'Process {self.ProcessOrder}::pid = {os.getpid()} ------------> task n° {self.taskOrder}' \
                    if self.taskOrder != None else f'Process {self.ProcessOrder}::pid = {os.getpid()}'

        pygame.display.set_caption(caption)

    def fill(self,rows,cols,boxsize,cols_startOffset,rows_startOffset,color):
        grid(self.screen,rows,cols,boxsize,cols_startOffset,rows_startOffset,color).drawGrid(True)

    def waitTillQuit(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()


class grid():
    def __init__(self,screen,rows,cols,boxsize,cols_startOffset,rows_startOffset,color):
        self.rows = rows
        self.cols = cols
        self.boxsize = boxsize
        self.cols_startOffset = cols_startOffset
        self.rows_startOffset = rows_startOffset
        self.grid = np.zeros((rows,cols))
        self.screen = screen
        self.color = color

    def drawGrid(self, slowly):
        for i in range(self.rows):
            for j in range(self.cols):
                self.__drawSmallbox(i, j)
                if(slowly == True):
                    for _ in range(DURATION):
                        pass
                pygame.display.update()

    def __drawSmallbox(self, r: int, c: int):
        box_Bg = (c * self.boxsize + self.rows_startOffset, r * self.boxsize + self.cols_startOffset, self.boxsize, self.boxsize)
        pygame.draw.rect(self.screen,self.color, box_Bg)



def singleThread_singleProcess():
    w = Window(900, 800)
    w.createwindow()
    startRowOffset = 10
    startColOffset = 50
    color = colors[0]
    for i in range(0, 4):
        w.fill(16, 80, 10, startRowOffset + i * 12 * 16, startColOffset, color)
        color = getNextColor(color)

    w.waitTillQuit()



def doTask(co,processOrder,taskOrder):
    w = Window(900, 13*13,processOrder,taskOrder)
    w.createwindow()
    startRowOffset = 10
    startColOffset = 50
    w.fill(14, 80, 10, startRowOffset , startColOffset, co)
    w.waitTillQuit()
    pass

def multiProcessingCall():
    windowStartY = 50
    allProcesses = []
    color = colors[0]
    for i in range(0, 4):
        p = Process(target=doTask, args=(color,i+1,i+1))
        setWindowsPosition(500, windowStartY + 13 * 17 * i)
        color = getNextColor(color)
        p.start()
        allProcesses.append(p)

    for p in allProcesses:
        p.join()



DURATION = 100000
# note : don't uncomment both lines together,when you uncomment one line , comment the other one .
if __name__ == "__main__":
    done = False
    while(not done):
        print("\nTo exist enter \'q\'")
        responce = input("use multiprocessing ? :[y/n]")
        if responce == "y":
            multiProcessingCall()
            print("--now answer with \'n\' to see how the uniprocessing works")
        elif responce == "n":
            singleThread_singleProcess()
            print("--now answer with \'y\' to see how the multiprocessing works")
        elif responce == 'q':
            done = True
        else:
            print("enter either \'n\' for \'no\' or \'y\' for \'yes\'")







#----end section 5------------------------------------------------------------------------------------