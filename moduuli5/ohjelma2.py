#!/usr/bin/env python3
import random

nums = []

while val := input("Syötä luku: "):
    nums.append(int(val))
    nums.sort(reverse=True)
    del nums[5:]

for n in nums:
    print(f"{n} ", end='')
print("")

