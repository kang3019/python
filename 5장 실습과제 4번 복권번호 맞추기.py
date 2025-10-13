#2자리 복권 복권 번호는  사용자가 입력, 당첨번호는 랜덤으로 생성하고 다 맞으면 100만원,1개 맞으면 50,아님 꽝
import random as r

#0~99까지 값을 n에 저장
n = r.randrange(100)

un = int(input("2자리 복권번호를 입력해주세요 : "))

#당첨 십의 자리수
tn = n//10
#당첨 일의 자리수
on = n%10
#입력 십의 자리수
tun = un//10
#입력 일의 자리수
oun = un%10

print(f"당첨 번호 {n}, 입력 번호 {un}")
if n == un :
    print("축하합니다 당첨입니다~!!!! 100만원권 ")
elif tn == tun or on == oun or tn == oun or on == tun:
    print("아쉬워요~ 한자리만 맞추셨습니다 50만원권 ")
else :
    print("꽝이에요~~~!!")

t.done()
        
