#!/usr/bin/env python
"""
Aufgabe 3: Rechteck
"""

from formen_neu import Shape

class Rectangle(Shape):
    """Klasse Rechteck"""

    def __init__(self, width, length):
        """Instantiierung der Attribute Länge und Breite"""
        Shape.__init__(self)
        self.width = width
        self.length = length

    def area(self):
        """Definition des Flächeninhalts"""
        return self.width * self.length

    def perimeter(self):
        """Definition des Umfangs"""
        return 2 * (self.width + self.length)

