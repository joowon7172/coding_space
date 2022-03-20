class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")


## super()의 문제점으로는 다중 상속을 할때 맨 앞쪽의 상속받는 클래스의 대해서만 super()이 적용이 된다.

class FlyableUnit1(Flyable, Unit):
    def __init__(self):
        super().__init__()

class FlyableUnit2(Unit, Flyable):
    def __init__(self):
        super().__init__()


## 그래서 다중상속에서 모든 부모클래스에 대해 초기화가 필요하다고 하면은 super() 대신에
class FlyableUnit3(Flyable, Unit):
    def __init__(self):
        Flyable.__init__(self)
        Unit.__init__(self)

## 앞에서 미리 배운 것 처럼 따로 해준다

dropship1 = FlyableUnit1()
dropship2 = FlyableUnit2()
print("\t")
dropship3 = FlyableUnit3()