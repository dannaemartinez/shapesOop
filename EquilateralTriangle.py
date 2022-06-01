from abc import ABC, abstractmethod
import os, math
from Shape import Shape  

class EquilateralTriangle(Shape):

    def __init__(self, _sideLength:float=1.0, _color:str="red", _filled:bool=True):
        super().__init__(_color, _filled)
        self._sideLength = _sideLength

    def getSideLength(self) -> float:
        return self._sideLength

    def setSideLength(self, _sideLength:float) -> float:
        self._sideLength = _sideLength

    def getArea(self) -> float:
        h = self._sideLength * (math.cos(math.pi/6))
        area = (self._sideLength * h)/2
        return area

    def getPerimeter(self) -> float:
        perimeter = 3 * self._sideLength
        return perimeter

    def __str__(self) -> str:
        return f'EquilateralTriangle[Shape[color={self._color}, filled={self._filled}, sideLength={self._sideLength}]]'