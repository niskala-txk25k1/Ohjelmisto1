#!/usr/bin/env python3
import random

def noppa():
    return random.randint(1, 6)

roll = 0
while roll != 6:
    roll = noppa()
    print(roll)

