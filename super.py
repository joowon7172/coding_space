## super



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



##pass##
# 건물
class BuildingUnit(Unit):
    def __init__(self,name,hp,location):

        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) ### 부모클래스 대신 앞에 써주는것. super로 초기화 할때는 self정보 안보내줌 ###

        self.location = location
        
    def build(self):
        print("{0} 방향에 {1} 하나를 짓습니다.[체력 {2}]".format(self.location, self.name, self.hp))

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
supply_depot.build()