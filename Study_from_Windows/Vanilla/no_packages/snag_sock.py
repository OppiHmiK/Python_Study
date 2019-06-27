import math as mt

class Animal:

    def __init__(self, age, height, color, xpos, ypos):
        self.age = age
        self.height = height
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.velocity = 0

    def sound(self):
        pass

class Horse(Animal):

    def __init__(self,age, height, color, xpos, ypos):
        Animal.__init__(self, age, height, color, xpos, ypos)

    def sound(self):
        print('Neigh')

    def run(self, xdistance, ydistance, time):
        self.xposition += xdistance
        self.yposition += ydistance
        t_distance = mt.sqrt((xdistance + xdistance)*(ydistance + ydistance))
        self.velocity = t_distance / time

class dog(Animal):

    def __init__(self, age, height, color, xpos, ypos):
        Animal.__init__(self, age, height, color, xpos, ypos)

    def sound(self):
        print('bow-bow')


if __name__ == '__main__':
    danbi = Horse(5, 160, 'brown', 0, 0)
    choco = dog(10, 100, 'black', 50, 30)

    danbi.sound()
    choco.sound()

