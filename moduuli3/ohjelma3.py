#!/usr/bin/env python3

gender = input("Sukupuoli [mies/nainen]? ").lower()

val_min = 0.0
val_max = 0.0

if (gender[0] == "n"):
    val_min = 117.0
    val_max = 175.0
elif (gender[0] == "m"):
    val_min = 134.0
    val_max = 195.0
else:
    print("Virheellinen sukupuoli")
    quit()


val = float(input("Hemoglobiiniarvo (g/l)? "))

if (val < val_min):
    print("Hemoglobiiniarvo on alhainen")
elif (val > val_max):
    print("Hemoglobiiniarvo on korkea")
else:
    print("Hemoglobiiniarvo on normaali")

