#!/usr/bin/env python3
import random

def filter_odd(arr):
    filt = []
    for n in arr:
        if n % 2 == 0:
            filt.append(n)
    return filt

array = []
array_len = random.randint(5, 20)
for n in range(array_len):
    array.append(random.randint(1, 10))

print(array)
print(filter_odd(array))


