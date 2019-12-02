#!/usr/bin/env python
"""
Aufgabe 3: Klassen
"""

# random, numpy und die zwei erstellten Module importieren
import random
import numpy as np
from kreis import Circle
from rechteck import Rectangle


class Formen(Rectangle, Circle):
    """Klasse Formen, die auf die Module Kreis und Rechteck zugreift"""

    def __init__(self, area_k, perimeter_k, area_r, perimeter_r):
        """Instantiierung der Attribute"""
        self.area_k = area_k
        self.perimeter_k = perimeter_k
        self.area_r = area_r
        self.perimter_r = perimeter_r


def zufallszahl():
    """Funktion definieren, die zufällig eine Zahl zwischen 1 und 50 auswählt"""
    number = np.random.randint(1, 50)
    return number


# Liste erstellen, die eine zufällige Anzahl an Kreisen und Rechtecken enthält
FORM = []
for i in range(10):
    SHAPE = random.choice(["Kreis", "Rechteck"])
    FORM.append(SHAPE)

# Listen erstellen, die die Flächeninhalte und Umfänge der Formen enthalten werden
AREAS_K = []
PERIMETERS_K = []
AREAS_R = []
PERIMETERS_R = []

# Interation über die Liste
for i in FORM:
    if i == "Kreis":
        radius = zufallszahl()
        K_i = Circle(radius)

        AREAS_K.append(K_i.area_k())
        PERIMETERS_K.append(K_i.perimeter_k())
    elif i == "Rechteck":
        width = zufallszahl()
        length = zufallszahl()
        R_i = Rectangle(width, length)

        AREAS_R.append(R_i.area_r())
        PERIMETERS_R.append(R_i.perimeter_r())

# Ausgabe der Anzahl und der durchschnittlichen Umfänge der Formen
print("Es gibt " + str(FORM.count("Rechteck")) + " Rechtecke in der Liste.")
print("Es gibt " + str(FORM.count("Kreis")) + " Kreise in der Liste.")
print("")
print("Der durchschnittliche Umfang aller Kreise beträgt " + str(np.mean(PERIMETERS_K)) + " m.")
print("Der durchschnittliche Umfang aller Rechtecke beträgt " + str(np.mean(PERIMETERS_R)) + " m.")
