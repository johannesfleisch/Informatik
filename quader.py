#!/usr/bin/env python
"""
Aufgabe 3: Quader
"""

from rechteck import Rectangle

class Quader(Rectangle):
    """Klasse Quader, die von der Klasse Rectangle erbt"""
    
    def __init__(self, length, width, hight):
        """Instantiierung der Attribute Länge, Breite und Höhe"""
        self.length = length
        self.width = width
        self.hight = hight
        
    def volume(self):
        """Definition des Volumens"""
        return self.length*self.width*self.hight