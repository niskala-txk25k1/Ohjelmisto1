#!/usr/bin/env python3
import math

leiviskät = float(input("Leiviskät: "))
naulat    = float(input("Naulat:    "))
luodit    = float(input("Luodit:    "))

naulat  += leiviskät * 20.0
luodit  += naulat * 32.0
grammat  = luodit * 13.3


print("Nykymittoina:")

# Modulolla jos se oli tehtävän idea:
# print(f"{int(grammat / 1000.0)} kg {grammat % 1000.0:.2f} g")

kilot    = math.floor(grammat / 1000.0)
grammat -= kilot * 1000.0

print(f"{kilot} kg {grammat:.2f} g")

