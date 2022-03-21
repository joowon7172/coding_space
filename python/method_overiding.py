## 메서드 오버라이딩

class Unit:
    #생성자
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    #지상 유닛 이동함수
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0}: {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit): #Unit클래스 상속받음
    
    #### 부모 클래스인 Unit의 생성자에 speed를 추가하였으므로 부모 클래스의 생성자에도 speed를 추가해준다 ####
    ## Speed 추가
    def __init__(self, name, hp, speed, damage):

        ## Speed 추가
        Unit.__init__(self, name, hp, speed) ## 상속할 클래스의 생성자를 상속받을 클래스 내에서 호출해준다.

        self.damage = damage

    # def attack(self, location):
    #     print("{0}: {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location,self.damage))

    # def damaged(self, damage):
    #     print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
    #     self.hp -= damage
    #     print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
    #     if self.hp <= 0:
    #         print("{0}: 파괴되었습니다.".format(self.name))


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

    ## 공중 유닛은 지상speed가 필요 없기 때문에 0으로 표시
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 0
        Flyable.__init__(self, flying_speed)

    def move(self,location):
        print("공중 유닛 이동")

        ## 공중 유닛은 Flyable 클래스의 fly를 통해 날아갈 수 있음!! ##
        self.fly(self.name, location)

#벌쳐: 지상 유닛, 기동성이 좋음
vulture  = AttackUnit("벌쳐",80, 10, 20)

#배틀크루저: 공중유닛, 다 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")

## 메서드 오버라이딩 배우기 전: fly함수는 Flyable 클래스의 함수인데 상속되있어서 사용가능
## 메서드 오버라이딩 배운 후: 
battlecruiser.fly(battlecruiser.name,"3시")

##  ==> 지상유닛, 공중유닛에 따라 써야하는 함수가 달라 매번 확인해줘야하는 불편함이 있다. ##

## 해결책: 메서드 오버라이딩으로 move함수를 쓰는 것만으로도 지상유닛, 공중유닛 둘다 출력되게 해보자
### FlyableAttackUnit 클래스의 move 함수 주목!!! ###

battlecruiser.move("3시")


