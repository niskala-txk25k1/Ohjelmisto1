#!/usr/bin/env python3

names = set()

while name := input("Syötä nimi: "):
    if name in names:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        names.add(name)

for name in names:
    print(name)

