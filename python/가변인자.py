#가변인자

def profile(name, age, *language): # *(가변인자)를 사용하여 서로 다른 개수의 값을 넣어 줄 수 있다.  
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ") #end는 따옴표 사이의 문자이후 바로 다음줄을 출력한다는 뜻
    for lang in language:
        print(lang, end=" ")

    print() #줄바꿈 print

profile("유재석", 20, "Python","C","C++","C#","JavaScript","Java")
profile("박명수", 25, "C")
