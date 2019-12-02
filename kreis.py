#!/usr/bin/env python
"""
Aufgabe 3: Kreis
"""

from math import pi


class Circle:
    """Klasse Kreis"""

    def __init__(self, radius):
        """Instantiierung des Attributs Radius"""
        self.radius = radius

    def area_k(self):
        """Definition des Flächeninhalts"""
        return self.radius**2 * pi

    def perimeter_k(self):
        """Definition des Umfangs"""
        return 2 * self.radius * pi
