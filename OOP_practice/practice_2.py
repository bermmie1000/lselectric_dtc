# 가로, 세로 정보을 갖고, 사각형의 면적을 계산하는 메서드를 갖는 Rectangle 클래스를 정의하고,
# 생성한 객체의 사각형의 면적을 출력하는 프로그램을 작성하십시오.


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


if __name__ == "__main__":
    print(Rectangle(4, 5).area())

