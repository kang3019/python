#random 라이브러리 호출 후 r로 별명지음
import random as r

print("산수 퀴즈에 오신 것을 환영합니다.\n")
#숫자를 0~10까지 랜덤으로 뽑음
n1 = r.randint(1,9)
n2 = r.randint(1,9)


#산수퀴즈식을 msg 변수에 하나의 문자열로 만들어 넣음
#※(이유는 input에는 하나의 문자열 밖에 들어가지 않음)

msg = str(n1) + " + " + str(n2) + " = "
ans = int(input(msg))
print(ans==n1+n2)

msg = str(n1) + " - " + str(n2) + " = "
ans = int(input(msg))
print(ans==n1-n2)


msg = str(n1) + " * " + str(n2) + " = "
ans = int(input(msg))
print(ans==n1*n2)

msg = str(n1) + " / " + str(n2) + " = "
ans = int(input(msg))
print(ans==n1/n2)

