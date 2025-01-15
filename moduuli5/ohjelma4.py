#!/usr/bin/env python3
import random

cities = []

for n in range(5):
    cities.append( input(f"Syötä {n+1}. kaupunki: ") )

for city in cities:
    print(city)
