# 반지름 정보를 갖고, 원의 면적을 계산하는 메서드를 갖는 Circle 클래스를 정의하고,
#  생성한 객체의 원의 면적을 출력하는 프로그램을 작성하십시오.


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def radius(self):
        return self.radius

    def area(self):
        return 3.14 * self.radius ** 2


if __name__ == "__main__":
    s1 = Circle(2)
    print(f"반지름이 {s1.radius}인 원의 면적은 {s1.area()}")
