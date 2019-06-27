class Quadrangle:

    # NOTE : __init__(생성자) 해당클래스가 다루는 데이터 정의
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    # NOTE : __del__(소멸자) 클래스 소멸시 호출
    def __del__(self):
        print("Quadrangle object is deleted")


square = Quadrangle(1, 2, 3)



