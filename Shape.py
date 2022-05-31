from abc import ABC, abstractmethod
import os, math

class Shape(ABC):

    def __init__(self, _color:str="red", _filled:bool=True):
        self._color = _color
        self._filled = _filled

    def getColor(self) -> str:
        return self._color

    def setColor(self, _color:str) -> str:
        self._color = _color

    def isFilled(self) -> bool:
        return self._filled

    def setFilled(self, _filled:bool) -> bool:
        self._filled = _filled

    @abstractmethod
    def getArea() -> float:
        pass

    @abstractmethod
    def getPerimeter() -> float:
        pass

    def __str__(self) -> str:
        return f'Shape[color= {self._color}, filled= {self._filled}]'