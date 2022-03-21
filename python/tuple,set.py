## 튜플 
## 리스트와 다르게 내용 변경, 추가 불가






## 집합
## 중복안됨, 순서없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

## 교집합
print(java & python)
print(java.intersection(python))


## 합집합
print(java | python)
print(java.union(python))


## 차집합
print(java - python)
print(java.difference(python))


python.add("김태호")
print(python)