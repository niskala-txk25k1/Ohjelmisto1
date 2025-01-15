#!/usr/bin/env python3
import sys

val = int(sys.argv[1] if len(sys.argv)==2 else input("Syötä luku: "))

for n in range(2, val):
    if (val % n == 0):
        print(f"Luku {val} ei ole alkuluku")
        quit()
print(f"Luku {val} on alkuluku")

