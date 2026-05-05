#숫자 맞추기 게임(10번 안에 못 맞출시 정답 공개)

import random as r

tries = 0
guess = 0
answer = r.randint(1,100)

print("1부터 100까지 사이 숫자를 맞추시오")

while guess != answer and tries < 10 :
    guess = int(input("숫자 입력"))
    tries += 1

    if guess < answer :
        print("낮음")
    if guess > answer :
        print("높음")



if guess == answer :
    print(f"축하합니다,정답은 {answer},시도횟수 {tries}")
else :
    print(f"정답은 {answer},시도횟수 {tries}")
