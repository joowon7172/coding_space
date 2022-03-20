"""
Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출력예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

"""

class House:
    #매물초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    #매물정보표시
    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

house1 = House("강남","아파트","매매","10억","2010년")
house2 = House("마포","오피스텔","전세","5억","2007년")
house3 = House("송파","빌라","월세","500/50","2000년")

#방법1
print("총 3대의 매물이 있습니다.")
house1.show_detail()
house2.show_detail()
house3.show_detail()

print("\t")

#방법2
houses = []

houses.append(house1)
houses.append(house2)
houses.append(house3)


print("총 {}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()



