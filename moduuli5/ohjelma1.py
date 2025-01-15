#!/usr/bin/env python3
import sys
import random

rolls = int(sys.argv[1] if len(sys.argv)==2 else input("Arpakuutioiden määrä? "))
total = 0

for n in range(rolls):
    total += random.randint(1, 6)

print(f"Arpakuutioiden summa: {total}")

