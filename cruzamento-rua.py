from threading import Thread
from threading import Semaphore
from time import sleep
from random import randint

import sys

#---------------------------------------------------
def carroA(sA, sB):
    while True:
        sA.acquire()
        print('Carro A Passou')
        sleep(2)
        sB.release()

    
#---------------------------------------------------
def carroB(sB, sC):
    while True:
        sB.acquire()
        print('Carro B Passou')
        sleep(2)
        sC.release()

#---------------------------------------------------
def carroC(sC, sD):
    while True:
        sC.acquire()
        print('Carro C Passou')
        sleep(2)
        sD.release()

#---------------------------------------------------
def carroD(sD, sA):
    while True:
        sD.acquire()
        print('Carro D Passou')
        sleep(2)
        sA.release()

#---------------------------------------------------

sA = Semaphore(1)
sB = Semaphore(0)
sC = Semaphore(0)
sD = Semaphore(0)

tA = Thread(target=carroA, args=[sA, sB])
tA.start()

tB = Thread(target=carroB, args=[sB, sC])
tB.start()

tC = Thread(target=carroC, args=[sC, sD])
tC.start()

tD = Thread(target=carroD, args=[sD, sA])
tD.start()

tA.join()
tB.join()
tC.join()
tD.join()