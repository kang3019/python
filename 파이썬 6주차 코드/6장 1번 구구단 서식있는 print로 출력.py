#구구단 중첩 for문을 사용하여 출력해보기


for i in range(10) : #0~9
    for dan in range(2,10) : #2단~9단
        if i == 0 :#단 제목 출력 
            print(f"=={dan}단==", end="   ")
        else :
            print("%d*%d =%2d" % (dan,i,dan*i), end="   ")
    print("\n")


for i in range(10) : #0~9
    for dan in range(9,1,-1) : #9단~2단
        if i == 0 :#단 제목 출력 
            print(f"=={dan}단==", end="   ")
        else :
            print("%d*%d =%2d" % (dan,i,dan*i), end="   ")
    print("\n")

