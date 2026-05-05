#무작위 2자리 숫자 산수퀴즈를 만들어 사용자의 답과 비교한 후 
#사용자에게 계속할지 물어봐서 yes라고 하면 산수퀴즈 계속하기

import random as r

while True :
    num1 = r.randrange(10,100)
    num2 = r.randrange(10,100)

    op_list = ["x","/","+","-"]
    op = r.choice(op_list)

    print(f'{num1} {op} {num2} = ?')
    user_answer = int(input("정답을 입력해주세요. : "))

    answer = 0

    if op == "x" :
        answer = num1 * num2
    elif op == "/" :
        answer = int(num1 /num2)
    elif op == "+" :
        answer = num1 + num2
    elif op == "-" :
        answer = int(num1-num2)

    if answer == user_answer :
        print("정답입니다!")
    else :
        print("오답입니다!")


    next_answer = input("계속하시겠습니까? (yes/no)")

    if next_answer == "yes" :
        continue
    else :
        break
print("프로그램을 종료합니다")
