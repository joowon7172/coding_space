# 클래스
# 클래스에 대한 지식이 없기에 너무나도 중요함  



class Unit:

    # __init__ : 파이썬에서 쓰이는 생성자. 객체가 만들어질때 자동으로 호출되는 부분
    # 객체: 클래스로부터 만들어지는 부분
    # 인스턴스 : 해당 클래스 타입의 객체, 메모리에 할당된 객체를 의미. 
    ##### 여기서는 marine이나 tank가 Unit 클래스의 인스턴스
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# Unit("마린",40,5)
# Unit("마린",40,5)
# Unit("탱크",150,30)

marine1 = Unit("마린",40,5) #인스턴스
marine2 = Unit("마린",40,5)  #인스턴스
tank = Unit("탱크",150,30)  #인스턴스

wraith1 = Unit("레이스",80, 5)
print("유닛이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.damage))


wraith2 = Unit("빼앗은 레이스",80, 5)

# 클래스에 없는 clocking 변수를 외부에서 추가로 할당
# 확장된 변수는 확장을 한 변수에만 적용이 되고 기존의 다른 객체에는 적용이 안된다.
wraith2.clocking = True
if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))