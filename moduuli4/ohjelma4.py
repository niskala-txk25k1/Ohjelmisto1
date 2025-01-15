#!/usr/bin/env python3
import random

secret = random.randint(1, 10)
while (guess := int(input("Arvaa arvo (1..10): "))) != secret:
    print(f'Liian {"suuri" if guess > secret else "pieni"} arvaus! ', end='')

print(f"Oikein! Arvo oli {secret}")
