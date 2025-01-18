#!/usr/bin/env python3
import sys

month = int(sys.argv[1] if len(sys.argv)==2 else input("Kuukauden numero? "))

seasons = "talvi", "kevät", "kesä", "syksy"
index = (month%12) // 3
print(seasons[index])
