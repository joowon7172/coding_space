#최소공배수를 구하는 알고리즘 구현

def lcm(a,b):
    xlist=[] # 일정범위 사이의 공배수를 저장하는 리스트

    for i in range(max(a,b), a*b+1):
        if(i % a == 0 and i % b == 0): # a와 b의 공배수이면 xlist 끝에 저장
            xlist.append(i)
    
    # xlist[0]이 최소공배수이다.
    print("%d와 %d의 최소공배수 = %d"%(a,b,xlist[0]))
        
lcm(60,28)
lcm(20,30)
lcm(7,13)
lcm(123,441)

