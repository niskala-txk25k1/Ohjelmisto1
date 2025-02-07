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

    key = input("ICAO-koodi: ")

    cur = con.cursor()
    cur.execute("SELECT name, municipality FROM airport WHERE ident=%s", (key,))

    for (name, municipality) in cur:
        print(f"{key}: {name}, {municipality}")

if __name__ == "__main__":
    main()
