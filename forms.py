from abc import ABC
from Circle import Circle
from Rectangle import Rectangle
from Square import Square
from EquilateralTriangle import EquilateralTriangle
# in this project double will be consider as float

if __name__ == '__main__':
    circulo = Circle(4, "blue", False)
    print("----------------Area del circulo--------------")
    print(circulo.getArea())
    print("-----------Perimetro del circulo--------------")
    print(circulo.getPerimeter())
    print(circulo)

if __name__ == '__main__':
    rec = Rectangle(6, 12, "reeed", False)
    print("--------------------Area del rectangulo-------------------")
    print(rec.getArea())
    print("--------------------Perimetro del rectangulo-------------------")
    print(rec.getPerimeter())
    print(rec)

if __name__ == '__main__':
    square = Square(5, "ggg", False)
    print("--------------------Area del cuadrado-------------------")
    print(square.getArea())
    print("--------------------Perimetro del cuadrado-------------------")
    print(square.getPerimeter())
    print(square)

if __name__ == '__main__':
    triangle = EquilateralTriangle(3, "rrrr", False)
    print("--------------------Area del triangulo-------------------")
    print(triangle.getArea())
    print("--------------------Perimetro del triangulo-------------------")
    print(triangle.getPerimeter())
    print(triangle)