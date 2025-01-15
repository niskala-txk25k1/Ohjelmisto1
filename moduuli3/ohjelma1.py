#!/usr/bin/env python3

cm = float(input("Kuhan pituus (cm)? "))

raja = 37.0

if(cm < raja):
    print(f"Laske kuha järveen. Kuhasi on {raja-cm:.2f} senttiä liian lyhyt.")
else:
    print("Voit pitää kuhasi :)")
