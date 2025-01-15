#!/usr/bin/env python3

w = float(input("Suorakulmion kanta (cm)?   "))
h = float(input("Suorakulmion korkeus (cm)? "))

circ = (w + h) * 2.0
area = w * h

print(f"Piiri:     {circ:.2f} cm")
print(f"Pinta-ala: {area:.2f} cm²")
