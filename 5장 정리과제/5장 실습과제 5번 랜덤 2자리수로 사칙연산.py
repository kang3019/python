#2개의 2자리 정수를 무작위로 생성해 사칙연산 문제 낸 후 사용자가 정답 입력 정답인지 오답인지 출력

import random as r

n1 = r.randrange(10,100)
n2 = r.randrange(10,100)


mesage = str(n1)+" + "+str(n2)+" = "
un = int(input(mesage))
if n1+n2 == un :
    print("정답")
else :
    print("오답")


mesage = str(n1)+" - "+str(n2)+" = "
un = int(input(mesage))
if n1-n2 == un :
    print("정답")
else :
    print("오답")

mesage = str(n1)+" * "+str(n2)+" = "
un = int(input(mesage))
if n1*n2 == un :
    print("정답")
else :
    print("오답")

mesage = str(n1)+" // "+str(n2)+" = "
un = int(input(mesage))
if n1//n2 == un :
    print("정답")
else :
    print("오답")
