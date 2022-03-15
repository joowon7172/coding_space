##다중 상속


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


# 드랍쉽

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0}: {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))



## 다중 상속은 클래스를 콤마로 구분해주면 됨

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


# 발키리: 공중 공격 유닛, 한번에 14발 미사일 발사

### 이러면 FlyableAttackUnit 클래스의 __init__함수의 name, hp, damage, flying_speed인수들이 "발키리", 200, 6, 5를 참조한다. 
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5) 

## FlyableAttackUnit클래스에 Flyable클래스가 상속되어 있으므로 Flyable 내의 함수를 FlyableAttackUnit클래스의 객체에서 사용 가능하다
valkyrie.fly(valkyrie.name, "3시") 
## 위의 문장 제대로 분석하기. 출력결과가 왜 이렇게 나오게 되는지 알고리즘 분석ㅣ
