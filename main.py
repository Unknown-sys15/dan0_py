#! /usr/bin/python2
#define interpreter -^
#which python2 -> terminalski ukaz


#ch mod -> change indetifier -> spremenis dovoljenje da lahko runas progr
# r   w   x
# 4   2   1
#Za izvajanje pozeni
#chmod +x main.py
#./main.py

import time

def main():#z main funkcijo omejim scope
    print "testic" #primer da tudi to dela ceprav podcrta
    time.sleep(0.1)
    print("Moje stevilo: %d" % 2)

if __name__== "__main__": #enviroment var
    main()






