# NOTE : (Public) public으로 선언된 attribute, method는 어떤 클래스라도 접근 가능

class Quadrangle:

    def __init__(self, width, height, color):

        self.width = width
        self.height = height
        self.color = color

    def get_area(self):
        return self.width * self.height

    def set_area(self, w, h):

        self.width = w
        self.height = h

# NOTE : (Protected)   protected로 선언된 attribute, method는 해당 클래스 또는 해당 클래스를 상속받은 클래스에서만 접근 가능
# NOTE : 파이썬의 해당속성 앞에 _를 붙임.

class Quadrangle2:

    def __init__(self, width, height, color):
        self._width = width
        self._height = height
        self._color = color

    def get_area(self):
        return self._width * self._height

    def _set_area(self, w, h):

        self._width = w
        self._height = h


# NOTE : (Private)  private로 선언된 attribute, method는 해당 클래스에서만 접근 가능
# NOTE : 파이썬의 attribute, method 앞에 __를 붙임.

class Quadrangle3:
    def __init__(self, width, height, color):
        self.__width = width
        self.__height = height
        self.__color = color

    def get_area(self):
        return self.__width * self.__height

    def __set_area(self, width, height):
        self.__width = width
        self.__height = height

''' square = Quadrangle(5, 5, 'black')
print(square.get_area())
print(square.width)
square.width = 10
print(square.get_area()) '''

''' square = Quadrangle2(5, 5, 'black')
print(square.get_area())
print(square._width)
square._width = 10
print(square.get_area())
square._set_area(3, 3)
print(square.get_area()) '''

square = Quadrangle(5, 5, "black")
print(square.__set_area(10, 10))

