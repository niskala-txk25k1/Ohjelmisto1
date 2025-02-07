#!/usr/bin/env python3

import mysql.connector

def main():
    con = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='metropolia',
        password='metropolia',
        autocommit=True
    )

    key = input("Maakoodi: ")

    cur = con.cursor()
    cur.execute("SELECT type FROM airport WHERE iso_country=%s", (key,))

    types = {}
    for (t,) in cur:
        if t not in types:
            types[t] = 0
        types[t] += 1

    for t in types:
        print(f"{t}: {types[t]}")

if __name__ == "__main__":
    main()
