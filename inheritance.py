#상속





## Unit클래스의 name, hp와 AttackUnit클래스의 name, hp가 겹친다
## 이때 상속을 사용하여 편리하게 이용할 수 있다
## 상속할 클래스의 생성자를 상속받을 클래스 내에서 호출해준다.

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit): #Unit클래스 상속받음
    
    def __init__(self, name, hp, damage):

        Unit.__init__(self, name, hp) ## 상속할 클래스의 생성자를 상속받을 클래스 내에서 호출해준다.

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