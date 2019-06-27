class circle():

    def __init__(self, __round, __name):
        self.__round = __round
        self.__name = __name

    def get_name(self):
        return self.__name

    def get_area(self):
        return 3.14 * self.__round**2

cir = circle(3, 'circle1')
print(cir.get_area())
