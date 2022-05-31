from abc import ABC, abstractmethod
import os, math
from Shape import Shape

class Rectangle(Shape):

    def __init__(self, _width:float=1.0, _length:float=1.0, _color:str="red", _filled:bool=True):
        super().__init__(_color, _filled)
        self._width = _width
        self._length = _length

    def getWidth(self) -> float:
        return self._width

    def setWidth(self, _width:float) -> float:
        self._width = _width

    def getLength(self) -> float:
        return self._length

    def setLength(self, _length:float) -> float:
        self._length = _length

    def getArea(self) -> float:
        area = self._length * self._width
        return area

    def getPerimeter(self) -> float:
        perimetro = 2 * (self._length + self._width)
        return perimetro

    def __str__(self) -> str:
        return f'Rectangle[Shape[color={self._color}, filled={self._filled}, width={self._width}, length={self._length}]]'