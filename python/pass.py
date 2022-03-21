## pass


class Unit:
    #생성자
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    #지상 유닛 이동함수
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0}: {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))



##pass##
# 건물
class BuildingUnit(Unit):
    def __init__(self,name,hp,location):

        ## 상속 내용임. 상속받은 부모클래스의 매개변수와 자식클래스의 생성자의 매개변수가 겹치므로
        ## 부모클래스.__init__()을 해주어 같은 변수들을 다시 선언 할 필요 없게 만든다.
        Unit.__init__(self, name, hp)
        # self.name = name
        # self.hp = hp

        self.location = location
        #pass # 아무것도 안하고 일단 넘어가기, 일단은 완성된것 처럼 보여짐

    def build(self):
        print("{0} 방향에 {1} 하나를 짓습니다.[체력 {2}]".format(self.location, self.name, self.hp))

#서플라이 디폿: 건물, 1개건물 = 8개 유닛 생성가능
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
supply_depot.build()


def game_start():
    print("새 게임 시작")

def game_over():
    pass    ## 아무것도 안하고 일단 넘어가기, 일단은 완성된 것 처럼 보이기

game_start()
game_over()