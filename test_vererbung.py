#!/usr/bin/env python
"""
Aufgabe 4: pytest
"""

from math import pi
import pytest
from vererbung_fuer_test import Circle, Rectangle, Quader


def test_for_circle_area():
    """Test für den Flächeninhalt eines Kreises"""
    assert Circle(1).area() == pi


def test_for_circle_perimeter():
    """Test für den Umfang eines Kreises"""
    assert Circle(1).perimeter() == 2*pi


def test_for_circle_volume():
    """Test für das Volumen eines Kreises"""
    assert Circle(1).volume() == "Die Berechnung des Volumens ist noch nicht näher spezifiziert."


def test_for_rectangle_area():
    """Test für den Flächeninhalt eines Rechtecks"""
    assert Rectangle(2, 2).area() == 4


def test_for_rectangle_perimeter():
    """Test für den Umfang eines Rechtecks"""
    assert Rectangle(2, 2).perimeter() == 8


def test_for_rectangle_volume():
    """Test für das Volumen eines Rechtecks"""
    assert Rectangle(2, 2).volume() == "Die Berechnung des Volumens ist noch nicht näher spezifiziert."


def test_for_quader_area():
    """Test für den Flächeninhalt eines Quaders"""
    assert Quader(2, 2, 2).area() == 4


def test_for_quader_perimeter():
    """Test für den Umfang eines Quaders"""
    assert Quader(2, 2, 2).perimeter() == 8


def test_for_quader_volume():
    """Test für das Volumen eines Quaders"""
    assert Quader(2, 2, 2).volume() == 8
