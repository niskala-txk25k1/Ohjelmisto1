#!/usr/bin/env python3
import sys
import random

val = int(sys.argv[1] if len(sys.argv)==2 else input("Nopan tahkoisuus? "))

def noppa(sides):
    return random.randint(1, sides)

roll = 0
while roll != val:
    roll = noppa(val)
    print(roll)

