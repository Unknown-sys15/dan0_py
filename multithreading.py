#! /usr/bin/python2

import time
from threading import Thread
import sys
from multiprocessing import Lock
###LOCK oz mutex je podobno semaforju samo da nima FIFO cakalne vrste
global thr1running, mx
thr1running = False
mx = Lock()

def thr1():
    global thr1running,mx
    thr1running = True
    num = 1
    numPrev = 1
    while thr1running:
        mx.acquire()
        temp = num
        num=num+numPrev
        numPrev = temp
        print(num)
        sys.stdout.flush() #da ne cakamo konec threada za dobit podatke
        time.sleep(0.5)
        mx.release()
        time.sleep(0.5)
        
def thr2():
    while True:
        print("Deamon thread")
        time.sleep(1)


def main():
    global thr1running,mx
    thr1obj = Thread(target=thr1,args=())
    thr1obj.start()

    thr2obj = Thread(target=thr2)
    thr2obj.setDaemon(True)
    thr2obj.start()

    try:
        while True:
            mx.acquire()
            print("Main thread")
            time.sleep(2)
            mx.release()
            time.sleep(0.5)
    except KeyboardInterrupt:
        mx.release()
        thr1running=False
        print("cakam na thread")
        thr1obj.join(0.5) #cakas da se ustavi iyvajat thread preden se zapre
        print("izhod")

if __name__== "__main__":
    main()