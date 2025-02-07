#!/usr/bin/env python3

import mysql.connector
from geopy.distance import geodesic

def get_airport(con, prompt):
    key = input(prompt)
    cur = con.cursor()
    query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident=%s"
    cur.execute(query, (key,))
    coords = cur.fetchone()
    if coords == None:
        print("Virheellinen ICAO-koodi")
        exit()
    return coords

def main():
    con = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='metropolia',
        password='metropolia',
        autocommit=True
    )

    src = get_airport(con, "ICAO-koodi 1: ")
    dst = get_airport(con, "ICAO-koodi 2: ")
    dist = geodesic(src, dst).km
    print(f"Etäisyys: {dist:.2f} km")

if __name__ == "__main__":
    main()
