#! /usr/bin/python2
import time
from copy import copy, deepcopy

def main():
	spisek1 = ["Franci","Peter","marusa"]
	spisek2 = spisek1

	temp = spisek1.pop(1)
	print(temp)
	print(repr(spisek1))
	print(repr(spisek2))

	spisek1.append(temp)
	print("spisek 1 po append "+ repr(spisek1))
	spisek3 = copy(spisek1)
	spisek3.pop(0)

	print("spisek 1"+ repr(spisek1))
	print("spisek 3"+ repr(spisek3))

if __name__== "__main__":
    main()


