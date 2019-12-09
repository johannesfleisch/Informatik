##!/usr/bin/env python
"""
Aufgabe 5: Schere/Stein/Papier
"""

# random importieren
import time
import random

# Einleitung
print("-------------------")
time.sleep(1.0)
print("Schere-Stein-Papier")
time.sleep(1.0)
print("-------------------")
time.sleep(1.0)
print("")

# Variablen für Spielstand erstellen
SCOREPLY = 0
SCORECOM = 0

# Liste erstellen
GAME = ["Schere", "Stein", "Papier"]

# While-Schleife festlegen
while True:
    # Eingabeabfrage für Spieler und Computer
    PLY1 = input("Schere/Stein/Papier?: ")
    PLY2 = random.choice(GAME)

    try:
        # Sieger ermitteln
        if PLY1 in GAME and PLY2 in GAME:
            if PLY1 == PLY2:
                print("Computer wählte auch: " + PLY2)
                print("Unentschieden!")
                print("")
            else:
                if PLY1 == "Schere":
                    print("Computer wählte: " + PLY2)
                    if PLY2 == "Stein":
                        print("Computer gewinnt!")
                        print("")
                        # Zählen des Speilstands
                        SCORECOM = SCORECOM + 1
                    else:
                        print("Du gewinnst!")
                        print("")
                        # Zählen des Spielstands
                        SCOREPLY = SCOREPLY + 1

                if PLY1 == "Stein":
                    print("Computer wählte: " + PLY2)
                    if PLY2 == "Papier":
                        print("Computer gewinnt!")
                        print("")
                        SCORECOM = SCORECOM + 1
                    else:
                        print("Du gewinnst!")
                        print("")
                        SCOREPLY = SCOREPLY + 1

                if PLY1 == "Papier":
                    print("Computer wählte: " + PLY2)
                    if PLY2 == "Schere":
                        print("Computer gewinnt!")
                        print("")
                        SCORECOM = SCORECOM + 1
                    else:
                        print("Du gewinnst!")
                        print("")
                        SCOREPLY = SCOREPLY + 1

        # else-Bedingung festlegen
        else:
            raise TypeError

    # except formulieren
    except TypeError:
        print("Falsche Eingabe, versuch's nochmal!")
        print("")

    # Festlegen, ob Spiel fortgesetzt oder abgebrochen wird
    if SCOREPLY >= 3:
        # While-Schleife beenden
        break
    elif SCORECOM >= 3:
        break

# Endstand ausgeben
print("-------------------")
time.sleep(1.0)
print("Danke fürs Spielen!")
time.sleep(1.0)
print("-------------------")
time.sleep(1.0)
print("")
print("Endstand:")
print("---------")
time.sleep(1.6)
print("Computer: " + str(SCORECOM))
time.sleep(1.6)
print("Spieler: " + str(SCOREPLY))
time.sleep(1.6)
print("")

if SCORECOM > SCOREPLY:
    print("Der Computer hat gewonnen.")
else:
    print("Gratuliere, du hast gewonnen!")
