#!/usr/bin/env python3

val_min = float('inf')
val_max = float('-inf')

while val := input("Syötä luku: "):
    valf = float(val)
    val_min = min(val_min, valf)
    val_max = max(val_max, valf)

print(f"Pienin luku: {val_min}")
print(f"Suurin luku: {val_max}")
