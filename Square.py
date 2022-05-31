from Rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, side:float=1.0, _color:str="red", _filled:bool=True):
        super().__init__(side, side, _color, _filled)


    def getSide(self) -> float:
        return self.getWidth()

    def setSide(self, side:float) -> float:
        self.setWidth(side)
        self.setLength(side)

    def setWidth(self, side:float) -> float:
        self._width = self._length = side

    def setLength(self, side:float) -> float:
        self._width = self._length = side
    
    def __str__(self) -> str:
        return f'Square[Rectangle[Shape[color={self._color}, filled={self._filled}, width={self._width}, length={self._length}]]]'