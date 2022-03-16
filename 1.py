#알고리즘 1.5

def gcd_2(a,b):
    alist=[]
    blist=[]

    for i in range(1,a+1):
        if a % i == 0:
            alist.append(i) #append 함수는 리스트형태의 데이터에 마지막에 하나를 추가하는 함수

    print(a,'의 약수 =',alist)

    for i in range(1,b+1):
        if b % i == 0:
            blist.append(i)

    print(b,'의 약수 =',blist)

    x=0 #최대공약수 변수

    for i in alist:
        for k in blist:
            if i == k:
                x=i

    print('%d와 %d의 최대공약수 = %d\n' %(a,b,x))


gcd_2(60,28)
gcd_2(20,30)
gcd_2(123, 441)

print('\n')


#알고리즘 1.6

def gcd_3(a,b):
    alist=[]

    for i in range(1,a+1):
        if a % i == 0: # a에서 i를 나눈 나머지가 0이면
            alist.append(i)
            
    print("%d의 약수 = %s" %(a,alist))
    #print(a,"의 약수 =",alist,")")

    alist.sort(reverse=True) #내림차순으로 정렬

    for i in alist:
        if b % i == 0: # b에서 i를 나눈 나머지가 0이면
            return i #제일 큰 수를 반환하기 때문이 이 값이 곧 최대공약수

    #print(a,'과',b,'의 최대공약수 = ',alist,'\n')

print('60과 28의 최대공약수 = ',gcd_3(60,28),'\n')
print('20과 30의 최대공약수 = ',gcd_3(20,30),'\n')
print('123과 441의 최대공약수 = ',gcd_3(123, 441),'\n')

print('\n')


#알고리즘 1.7

def gcd_4(a,b): #a가 b보다 작지 않아야 함
    print("gcd(%d,%d)"%(a,b))
    while b != 0:
        r = a % b   # a 나누기 b의 나머지를 r에 저장
        a = b       # b를 a에 저장
        b = r       # r을 b에 저장

        print("gcd(%d,%d)"%(a,b))

    return a


print("60과 28의 최대공약수=%d\n"%gcd_4(60,28))
print("30과 20의 최대공약수=%d\n"%gcd_4(30,20))
print("441과 123의 최대공약수=%d\n"%gcd_4(441,123))

print('\n')

#----------------------------------------------

#a가 b보다 작은 경우

def gcd_5(a,b): 
    print("gcd(%d,%d)"%(a,b))
    while b != 0:   # b가 0이 아닐때
        if(a < b):  # a가 b보다 작을때 a b 값 바꾸기
            temp = a
            a = b
            b = temp

        r = a % b   # a 나누기 b의 나머지를 r에 저장
        a = b       # b를 a에 저장
        b = r       # r을 b에 저장

        print("gcd(%d,%d)"%(a,b))

    return a


print("60과 28의 최대공약수=%d\n"%gcd_5(60,28))
print("20과 30의 최대공약수=%d\n"%gcd_5(20,30))
print("123과 441의 최대공약수=%d\n"%gcd_5(123,441))



