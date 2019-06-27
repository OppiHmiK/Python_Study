from pprint import pprint

class Quadrangle:
    width = 0
    height = 0
    color = 'black'
    
class Dave:
    data = 0
    name = 'dave'

square = Quadrangle()
square2 = Quadrangle()

print(square.color)
square2.color = 'red'
print(square2.color)

square.width = 5
print(square.width, square2.width)
