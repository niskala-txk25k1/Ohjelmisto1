#!/usr/bin/env python3
import math

def price_per_m2(diam, price):
    area = math.pi * (diam/2.0)**2
    return price/area


lowest_index = -1
lowest_value = float('inf')

for i in range(2):
    i+=1
    diam =  float(input(f"Pitsan {i} halkaisija (cm)? "))
    price = float(input(f"Pitsan {i} hinta (€)?       "))

    diam /= 100.0 # cm -> m
    value = price_per_m2(diam, price)
    print(f"{value:.2f} €/m²")

    if (value < lowest_value):
        lowest_value = value
        lowest_index = i
    print("")

print(f"Pitsa {lowest_index} on halvin.")
