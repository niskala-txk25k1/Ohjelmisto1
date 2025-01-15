#!/usr/bin/env python3

db = {"EFHK": "Helsinki-Vantaan lentoasema"}

while True:
    cmd = input("Syötä komento [lisää/hae/lopeta]: ").lower()

    if (cmd == "lopeta"):
        break

    elif (cmd == "hae"):
        code = input("Syötä haettava ICAO-koodi: ").upper()
        if code in db:
            print( db[code] )
        else:
            print("Tuntematon ICAO-koodi")

    elif (cmd == "lisää"):
        code = input("Syötä lisättävä ICAO-koodi: ").upper()
        name = input("Syötä lentoaseman nimi:     ")
        db[code] = name

    print("")

