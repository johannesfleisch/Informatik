#!/usr/bin/env python
"""
Aufgabe 3: Klassen
"""

# numpy und die zwei erstellten Module importieren
import numpy as np
from kreis import Circle
from rechteck import Rectangle


class Formen(Circle, Rectangle):
    """Klasse Formen, die auf die Module Kreis und Rechteck zugreift"""

    def __init__(self, area_k, perimeter_k, area_r, perimeter_r):
        self.area_k = area_k
        self.perimeter_k = perimeter_k
        self.area_r = area_r
        self.perimeter_r = perimeter_r


def zufallszahl():
    """Funktion definieren, die zufällig eine Zahl zwischen 1 und 50 auswählt"""
    number = np.random.randint(1, 50)
    return number


# Variablen definieren, die den Modulen eine Zufallszahl zuweisen
KREIS = Circle(zufallszahl())
RECHTECK = Rectangle(zufallszahl(), zufallszahl())

# Ausgabe der Flächeninhalte und Umfänge der Formen
print("Der Flächeninhalt des Kreises beträgt " + str(KREIS.area_k()) + " m².")
print("Der Umfang des Kreises beträgt " + str(KREIS.perimeter_k()) + " m.")
print("Der Flächeninhalt des Rechtecks beträgt " + str(RECHTECK.area_r()) + " m².")
print("Der Umfang des Rechtecks beträgt " + str(RECHTECK.perimeter_r()) + " m.")
