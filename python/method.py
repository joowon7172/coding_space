# 메소드



class Unit:

    # __init__ : 파이썬에서 쓰이는 생성자. 객체가 만들어질때 자동으로 호출되는 부분
    # 객체: 클래스로부터 만들어지는 부분
    # 인스턴스 : 해당 클래스 타입의 객체, 메모리에 할당된 객체를 의미, 인스턴스란, 클래스를 실체화한 것이다. 
    ##### 여기서는 marine이나 tank가 Unit 클래스의 인스턴스
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

class AttackUnit:

    ##### self : 자기 자신을 의미, 클래스내에서 메소드앞에는 항상 self를 적어준다고 이해하면 됨 ####
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0}: {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location,self.damage))

    def damaged(self, damage):
        print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16) #firebat1 은 AttackUnit클래스의 객체
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)