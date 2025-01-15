#!/usr/bin/env python3

print("Syötä 3 kokonaislukua.")
a = int(input("1. kokonaisluku: "))
b = int(input("2. kokonaisluku: "))
c = int(input("3. kokonaisluku: "))

print(f"Syötit luvut {a}, {b} ja {c}")

summa = a + b + c
tulo  = a * b * c
keskiarvo = summa / 3.0

print(f"Summa:     {summa}")
print(f"Tulo:      {tulo}")
print(f"Keskiarvo: {keskiarvo:.2f}")
