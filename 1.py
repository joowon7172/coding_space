# 전달값과 반환값

def open_account():
    print("새로운 계좌 생성")

def deposit(balance, money): #입금 함수
    print("입금 완료. 잔액 {0} 원.".format(balance + money))
    return balance + money 

def withdraw(balance, money):
    if balance >= money:# 잔액이 출금보다 많을 때
        print("출금 완료. 잔액 {0} 원".format(balance - money))
        return balance - money
    else: # 잔액이 출금보다 적을때
        print("출금 불가. 잔액 {0} 원".format(balance))
        return(balance)


balance = 0 # 잔액

# return을 통해서 반환된 수를 balance가 참조
balance = deposit(balance, 1000) 
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
