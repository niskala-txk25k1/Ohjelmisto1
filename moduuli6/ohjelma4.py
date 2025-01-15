#!/usr/bin/env python3
import random

def list_sum(arr):
    total = 0
    for n in arr:
        total += n
    return total

array = []
array_len = random.randint(5, 20)
for n in range(array_len):
    array.append(random.randint(1, 10))

print(array)
print(list_sum(array))


