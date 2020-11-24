from threading import Thread
from threading import Semaphore
from time import sleep
from random import randint

import sys

#---------------------------------------------------
rc = 0
nflorestaalta = 5
ngranderio = 1

#---------------------------------------------------
def florestaalta(tid, p, mutex):
    global rc

    while True:

        mutex.acquire()
        rc = rc + 1
        if rc == 1:
            p.acquire()
        mutex.release()

        print('Viajante Floresta Alta %d atravessou a ponte' % tid)

        mutex.acquire()
        rc = rc - 1
        if rc == 0:
            p.release()
        mutex.release()

        sleep(5)
    
#---------------------------------------------------
def granderio(tid, p):
   
     while True:
        p.acquire()
        print('Viajante Grande Rio %d atravessou a ponte' % tid)
        p.release()
        sleep(5)
        
#---------------------------------------------------

p = Semaphore(1)
mutex = Semaphore(1)

l = []
for i in range(nflorestaalta):
    tf = Thread(target=florestaalta, args=[i, p, mutex])
    l.append(tf)    
    tf.start()

e = []
for i in range(ngranderio):
    tg = Thread(target=granderio, args=[i, p])
    l.append(tg)
    tg.start()

for tf in l:
    tf.join()

for tg in e:
    tg.join()



