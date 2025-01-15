#!/usr/bin/env python3
import sys

year = int(sys.argv[1] if len(sys.argv)==2 else input("Vuosi? "))

if (year % 4 == 0) and not ((year % 100 == 0) and (year % 400 != 0)): # sori
    print(f"Vuosi {year} on karkausvuosi")
else:
    print(f"Vuosi {year} ei ole karkausvuosi")
