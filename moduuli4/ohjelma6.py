#!/usr/bin/env python3
import random

rolls = int(input("Arvottavien pisteiden määrä: "))
hits  = 0
i     = 0
while (i:=i+1) <= rolls:
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    hits += (x**2.0 + y**2.0 < 1.0)

print( f"{hits/rolls*4.0}" )
