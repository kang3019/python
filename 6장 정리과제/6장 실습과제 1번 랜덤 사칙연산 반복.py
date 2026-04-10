import random as r

while True :
    n1 = r.randrange(10,100)

    n2 = r.randrange(10,100)


    f = ["+","-","*","//"]

    f1 = r.choice(f)



    result = 0

    if f1 == "+" :
        result = n1+n2
    elif f1 == "-" :
        result = n1-n2
    elif f1 == "*" :
        result = n1*n2
    elif f1 == "//" :
        result = n1//n2
        
    while True :
        user = int(input(f"{n1} {f1} {n2} = "))

        if user == result :
            print("정답입니다")
            break
        else :
            print("틀렸습니다 다시 시도하세요")
    

    cho = input("계속 문제를 풀겠습니까??? (y/n)")

    if cho == "y" :
        continue
    elif cho == "n" :
        break


