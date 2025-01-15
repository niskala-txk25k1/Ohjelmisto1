#!/usr/bin/env python3

username = "python"
password = "rules"
tries = 1+5

while (tries:=tries-1):
    print(f"Kirjaudu ({tries} yritys(tä) jäljellä).")
    in_user = input("Käyttäjä: ")
    in_pass = input("Salasana: ")
    if in_user == username and in_pass == password:
        print("Tervetuloa")
        quit()

print("Pääsy evätty")
