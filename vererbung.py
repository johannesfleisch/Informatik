##!/usr/bin/env python
"""
Aufgabe 3: Klassen
"""

# random, numpy und die zwei erstellten Module importieren
import random
import numpy as np
from math import pi


class Shape:
    """Klasse Shape"""

    def __init__(self):
        """keine Instantiierung"""
        pass

    def area(self):
        """keine Rückgabe"""
        return None

    def perimeter(self):
        """keine Rückgabe"""
        return None

    def volume(self):
        """Rückgabe eines Strings"""
        return "Die Berechnung des Volumens ist noch nicht näher spezifiziert."

    def info(self):
        print("Diese Figur hat eine Fläche von " + str(self.area()) + " m² und einen Umfang von " + str(self.perimeter()) + "m.")


class Rectangle(Shape):
    """Klasse Rechteck"""

    def __init__(self, width, length):
        """Instantiierung der Attribute Länge und Breite"""
        self.width = width
        self.length = length

    def area(self):
        """Definition des Flächeninhalts"""
        return self.width * self.length

    def perimeter(self):
        """Definition des Umfangs"""
        return 2 * (self.width + self.length)


class Circle(Shape):
    """Klasse Kreis"""

    def __init__(self, radius):
        """Instantiierung des Attributs Radius"""
        self.radius = radius

    def area(self):
        """Definition des Flächeninhalts"""
        return self.radius**2 * pi

    def perimeter(self):
        """Definition des Umfangs"""
        return 2 * self.radius * pi


class Quader(Rectangle):

    def __init__(self, length, width, hight):
        """Instantiierung der Attribute Länge, Breite und Höhe"""
        self.length = length
        self.width = width
        self.hight = hight

    def volume(self):
        """Definition des Volumens"""
        return self.length*self.width*self.hight


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

        AREAS_K.append(K_i.area())
        PERIMETERS_K.append(K_i.perimeter())
    elif i == "Rechteck":
        width = zufallszahl()
        length = zufallszahl()
        R_i = Rectangle(width, length)

        AREAS_R.append(R_i.area())
        PERIMETERS_R.append(R_i.perimeter())

# Ausgabe der Anzahl und der durchschnittlichen Umfänge der Formen
print("Es gibt " + str(FORM.count("Rechteck")) + " Rechtecke in der Liste.")
print("Es gibt " + str(FORM.count("Kreis")) + " Kreise in der Liste.")
print("")
print("Der durchschnittliche Umfang aller Kreise beträgt " + str(np.mean(PERIMETERS_K)) + " m.")
print("Der durchschnittliche Umfang aller Rechtecke beträgt " + str(np.mean(PERIMETERS_R)) + " m.")
print("")
print("Das Volumen des Quaders beträgt " + str(Quader(3, 3, 3).volume()) + " m³.")