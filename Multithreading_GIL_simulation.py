#Topic 3 : simulation on how the GIL works:
"""
summary:
In this section we created a small simulation that presents three threads,
These three threads will not be executed in parallel because of the global
interpreter lock (GIL) so each thread will start working only when acquiring the GIL lock
"""


import threading
import time
from time import sleep
from typing import List

class simulation:
    @staticmethod
    def gilConstraint():
        for j in range(1, 4):
            print(f'Thread -{j}- : (GIL) ', end="")
            progress = ""
            for i in range(50):
                print("*", end="")
                progress += "*"

                percentage = int(i * 100 / 49)
                print("", end="\r")
                print(f'Thread -{j}- : (GIL) ', end=f"< {percentage} %> ")
                print(progress, end="")

                time.sleep(.12)

            print("", end="\r")
            print(f'Thread -{j}- : (   ) ', end=f"< {percentage} %> ")
            print(progress, end="\n")

if __name__ == "__main__":
    print('SUMMARY: \n\n'
          'In this section, we created a small simulation that presents three threads. \n'
          'These three threads will not be executed in parallel because of the global \n'
          'interpreter lock (GIL), so each thread will start working only when acquiring the GIL lock\n')

    responce = input("-----start GIL(global interperter lock) constraint simulation ? [y/n] :")
    if responce in ["y","yes","ye"]:
        simulation.gilConstraint()
    input()

