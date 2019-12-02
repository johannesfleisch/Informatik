#!/usr/bin/env python
"""
Aufgabe 3: Rechteck
"""


class Rectangle:
    """Klasse Rechteck"""

    def __init__(self, width, length):
        """Instantiierung der Attribute Länge und Breite"""
        self.width = width
        self.length = length

    def area_r(self):
        """Definition des Flächeninhalts"""
        return self.width * self.length

    def perimeter_r(self):
        """Definition des Umfangs"""
        return 2 * (self.width + self.length)
