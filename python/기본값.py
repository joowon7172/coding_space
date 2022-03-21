# 기본값


#같은 학교, 같은 학년, 같은 반, 같은 수업.
def profile1(name, age = 24, main_lang = "파이썬"):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name, age, main_lang))

profile1("유재석")
profile1("박명수")

def profile2(name, age, main_lang):
    print(name, age, main_lang)

profile2(name = "유재석", main_lang="파이썬", age=20)
profile2(main_lang="자바", age=25, name="박명수")









