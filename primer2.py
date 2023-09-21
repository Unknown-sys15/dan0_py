#! /usr/bin/python2

import time
from collections import deque

def main():
    for i in range(1,10):
        print(str(i))

    spisek = [2,4,5,7,8,4] # linked list
    print(" ")

    for j in range(len(spisek)):
        print(str(spisek[j]))
    print(" ")

    for el in spisek:
        print(str(el))
    print(" ")

    for i,l in enumerate(spisek):
        print("ind %d: %d" % (i,el)) #touple -> immutable

    #list comprehantion
    spisek2 = [k for k in spisek if k>3]
    print(repr(spisek2))

    #dictionary
    dict1 = {"Peter":"020182515",
             "Franci":"02018448"}
    for key, el in dict1.items():
        print(el+" "+key) 
    for key, _ in dict1.items(): #podcrtaj ko te ne zanima sprem
        print(key) 

    try:
        while True:
            print("beseda")
            time.sleep(1)
    except KeyboardInterrupt as e: #Exception as e ya catch all
        print(e)
    finally:
        print("Exiting")

    for m in range(0,10,2):
        print(" ")
    for m in range(10,0,-1):
        print(" ")

    #raw_input za tejkat input iy command lina
    #input se uporablja za poganjat ukaze
    asd = raw_input("vpisi nekaj: ")
    print(asd)


    #ko je vec kot 10 podatkov v queue brise najstarejse podatke
    d=deque(maxlen=10)
    d.append("nekaj")
    
if __name__== "__main__":
    main()
