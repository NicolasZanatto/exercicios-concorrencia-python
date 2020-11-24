from threading import Thread
from threading import Semaphore
from time import sleep
from random import randint

import sys

#---------------------------------------------------
rc = 0
nleitores = 3
nescritores = 1

#---------------------------------------------------
def leitor(tid, db, mutex):
    global rc

    while True:

        mutex.acquire()
        rc = rc + 1
        if rc == 1:
            db.acquire()
        mutex.release()

        print('Leitor: %d acessou a base' % tid)
        sleep(5)

        print('Leitor %d liberou a base' % tid)

        mutex.acquire()
        rc = rc - 1
        if rc == 0:
            db.release()
        mutex.release()

        sleep(5)
    
#---------------------------------------------------
def escritor(tid, db):
   
     while True:
        db.acquire()
        print('Escritor %d acessou a base' % tid)
        sleep(5)
        print('Escritor %d liberou a base' % tid)
        db.release()
        sleep(5)
        
#---------------------------------------------------

db = Semaphore(1)
mutex = Semaphore(1)

l = []
for i in range(nleitores):
    tl = Thread(target=leitor, args=[i, db, mutex])
    l.append(tl)    
    tl.start()

e = []
for i in range(nescritores):
    te = Thread(target=escritor, args=[i, db])
    l.append(te)
    te.start()

for tl in l:
    tl.join()

for te in e:
    te.join()



