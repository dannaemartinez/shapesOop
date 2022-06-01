from abc import ABC, abstractmethod
import os, math
from Shape import Shape  

class Circle(Shape):

    def __init__(self, _radius:float=1.0, _color:str="red", _filled:bool=True):
        self.setColor(_color)
        self.setFilled(_filled)
        self._radius = _radius

    def getRadius(self) -> float:
        return self._radius

    def setRadius(self, _radius:float) -> float:
        self._radius = _radius
    
    def getArea(self) -> float:
        area = math.pi * (self._radius ** 2)
        return area

    def getPerimeter(self) -> float:
        perimeter = 2 * math.pi * self._radius
        return perimeter

    def __str__(self) -> str:
        return f'Circle[Shape[color={self._color}, filled={self._filled}, radius={self._radius}]]'