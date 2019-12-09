#!/usr/bin/env python
"""
Aufgabe 3: Kreis
"""

from math import pi
from formen_neu import Shape

class Circle(Shape):
    """Klasse Kreis"""

    def __init__(self, radius):
        """Instantiierung des Attributs Radius"""
        Shape.__init__(self)
        self.radius = radius

    def area(self):
        """Definition des Flächeninhalts"""
        return self.radius**2 * pi

    def perimeter(self):
        """Definition des Umfangs"""
        return 2 * self.radius * pi