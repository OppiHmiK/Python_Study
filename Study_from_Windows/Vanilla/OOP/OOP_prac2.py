class Quadrangle:

    width = 0
    height = 0
    color = 'black'

    def get_area(self):
        return self.width * self.height

    def set_area(self, data1, data2):
        self.width = data1
        self.height = data2

square = Quadrangle()
square.set_area(5, 5)

print(square.width)
print(square.height)
print(square.get_area())