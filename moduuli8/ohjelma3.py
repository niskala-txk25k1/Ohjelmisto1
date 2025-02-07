#!/usr/bin/env python3

import mysql.connector
from geopy.distance import geodesic

def get_airport(con):
    key = input("ICAO-koodi: ")
    query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident=%s"
    cur = con.cursor()
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

    a = get_airport(con)
    b = get_airport(con)
    dist = geodesic(a, b).km
    print(f"{dist:.2f} km")

if __name__ == "__main__":
    main()
