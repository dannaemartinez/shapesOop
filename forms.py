from tokenize import Double
from xmlrpc.client import boolean
from abc import ABC, abstractmethod
import os, math


class Shape(ABC):
    _color = "red"
    _filled = True

    #Shape()
    # def __init__(self):
    #     pass

    def __init__(self, *args):
        if len(args) == 2:
            self._color = args[0]
            self._filled = args[1]

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


class Circle(Shape):
    _radius = 1.0

    def __init__(self, *args):
        super().__init__()
        if len(args) == 1:
            self._radius = args[0]
        elif len(args) == 3:
            self._radius = args[0]
            self._color = args[1]
            self._filled = args[2]

    def getRadius(self) -> float:
        return self._radius

    def setRadius(self, _radius:float) -> float:
        self._radius = _radius
    
    def getArea(self, _radius:float) -> float:
        area = math.pi * (_radius ** 2)
        return area

    def getPerimeter(self, _radius:float) -> float:
        perimetro = 2 * math.pi * _radius
        return perimetro

    def __str__(self) -> str:
        return f'Circle[{super(Circle, self).__str__()}, radius={self._radius}]'

class Rectangle(Shape):
    _width = 1.0
    _length = 1.0

    def __init__(self, *args):
        super().__init__()
        if len(args) == 2:
            self._width = args[0]
            self._length = args[1]
        elif len(args) == 4:
            self._width = args[0]
            self._length = args[1]
            self._color = args[2]
            self._filled = args[3]

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
        return f'Rectangle[{super(Rectangle, self).__str__()}, width={self._width}, length={self._length}]'

class EquilateralTriangle(Shape):
    _sideLength = 1.0

    def __init__(self, *args):
        super().__init__()
        if len(args) == 1:
            self._sideLength = args[0]
        elif len(args) == 3:
            self._sideLength = args[0]
            self._color = args[1]
            self._filled = args[2]

    def getSideLenght(self) -> float:
        return self._sideLength

    def setSideLength(self, _sideLength:float) -> float:
        self._sideLength = _sideLength

    def getArea(self) -> float:
        h = self._sideLength * (math.cos(math.pi/6))
        area = (self._sideLength * h)/2
        return area

    def getPerimeter(self) -> float:
        perimetro = 3 * self._sideLength
        return perimetro

    def __str__(self) -> str:
        return f'EquilateralTriangle[{super(EquilateralTriangle, self).__str__()}, sideLength={self._sideLength}]'

class Square(Rectangle):

    def __init__(self, *args):
        super().__init__()
        if len(args) == 1:
            self._length = self._width = args[0]
        elif len(args) == 3:
            self._length = self._width = args[0]
            self._color = args[1]
            self._filled = args[2]

    def getSide(self) -> float:
        return self._width

    def setSide(self, side:float) -> float:
        self._width = self._length = side

    def setWidth(self, side:float) -> float:
        self._width = self._length = side

    def setLength(self, side:float) -> float:
        self._width = self._length = side
    
    def __str__(self) -> str:
        return f'Square[{super(Square, self).__str__()}]'

circulo = Circle()
circulo.setRadius(3)
print("----------------Area del circulo--------------")
print(circulo.getArea(4))
print("-----------Perimetro del circulo--------------")
print(circulo.getPerimeter(4))
print(circulo)

rec = Rectangle()
rec.setLength(3)
rec.setWidth(6)
print("--------------------Area del rectangulo-------------------")
print(rec.getArea())
print("--------------------Perimetro del rectangulo-------------------")
print(rec.getPerimeter())
print(rec)

square = Square()
square.setSide(5)
print("--------------------Area del cuadrado-------------------")
print(square.getArea())
print("--------------------Perimetro del cuadrado-------------------")
print(square.getPerimeter())
print(square)

triangle = EquilateralTriangle()
triangle.setSideLength(3)
print("--------------------Area del triangulo-------------------")
print(triangle.getArea())
print("--------------------Perimetro del triangulo-------------------")
print(triangle.getPerimeter())
print(triangle)