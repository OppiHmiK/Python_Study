class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def Move(self,x,y):
        self.x += x
        self.y += y

    def Draw(self):
        print("중심 좌표 : ("+str(self.x) +", "+str(self.y)+")")

class Circle(Shape):
    def __init__(self,x,y,radius):
        super().__init__(x,y)
        self.radius = radius

    def __add__(self,pt1,pt2):
        pt1 = Circle(self.x + self.y)
        pt2 = Circle(self.radius + self.radius)
        return pt1, pt2

    def Draw(self):
        print("<<< 원 >>>")
        Shape.Draw(self)
        print("반지름 : "+str(self.x + self.y)+"")

class Rect(Shape):
    def __init__(self,x,y,p,q):
        super().__init__(x,y)
        self.p = p
        self.q = q

    def __add__(self,tp1,tp2,tp3):
        tp1 = Circle(self.x+self.y)
        tp2 = Circle(self.p + self.p)
        tp3 = Circle(self.q + self.q)
        return tp1, tp2, tp3

    def Draw(self):
        print("<<< 사각형  >>>")
        Shape.Draw(self)
        print("가로, 세로 : ("+str(self.p + self.p)+","+str(self.q + self.q)+")")

shape_list = [Circle(300, 200, 50), Circle(200, 100, 25), Rect(300, 200, 40, 60), Rect(100, 100, 70, 15)]
shape_list[1].Move(50, 50)
shape_list[3].Move(50, 50)


for shape in shape_list:
    shape.Draw()