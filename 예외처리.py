## 예외처리


### 숫자 입력에 문자를 입력하거나 하면 오류가 발생하면서 출력이 안된다.

# print("나누기 전용 계산기 입니다.")
# num1 = int(input("첫번째 숫자를 입력하세요: "))
# num2 = int(input("두번째 숫자를 입력하세요: "))
# print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
#########

## 이럴때 try except예외 처리 구문을 써 준다
## 동작방법은 우선 try내의 코드를 돌리다가 어떤 에러가 뜨면 except로 선언 한 것 중 알맞는 예외처리를 찾고 있으면 except내부의 코드를 실행시킨다. 

try:
    print("나누기 전용 계산기 입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요: "))
    num2 = int(input("두번째 숫자를 입력하세요: "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

    #올바른 값을 입력하지 않았을 때 뜨는 에러
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")

    ## ZeroDivisionError: 0을 분모로 놓았을때뜨는 에러 
except ZeroDivisionError as err:
    print(err)


