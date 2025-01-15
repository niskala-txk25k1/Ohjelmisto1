#!/usr/bin/env python3

def gal_to_liter(gal):
    return gal*3.785

while (gal := float(input("Syötä arvo (gallona): "))) >= 0:
    print(f"{gal:.2f} gallonaa on {gal_to_liter(gal):.2f} litraa")

