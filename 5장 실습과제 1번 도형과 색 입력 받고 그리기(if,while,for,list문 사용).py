#사용자에게 입력받아 해당 다각형 그리기


import turtle as t


#무한 반복
while True :
    #사용자에게 입력받기
    n = int(t.textinput("","몇각형을 그릴까요?"))

    #리스트 안에 색 저장
    list = ["red","yellow","blue","green","black"]

    #사용자에게 색 입력받기
    c = int(t.textinput(""," 어떤 색깔로 그릴까요?  (1,red 2:yellow 3:blue, 4: green, 5: black)")) 



    #해당 다각형 그릴 곳으로 이동
    t.up()
    t.goto(-50,-50)
    t.down()

    #숫자 입력받아 도형 그리기
    if n == 0 :
        #도형 그릴 색을 리스트로 받아옴
        t.fillcolor(list[c-1])
        #채우기 시작
        t.begin_fill()

        t.circle(50)

        #채우기 끝
        t.end_fill()

    elif n == 1 or n == 2 or n == 7 :
        t.write("0,또는 3~6,8 만 입력해주세요.")
    elif n ==3 or n ==4 or n ==5 or n ==6 or n ==8 :
        #해당 다각형의 한변의 각 구하기
        angle = 360/n
        
        #도형 그릴 색을 리스트로 받아옴
        t.fillcolor(list[c-1])
        #채우기 시작
        t.begin_fill()

        #해당 각형 수 만큼 반복
        for x in range(n) :
            t.fd(100)
            t.left(angle)
            
        #채우기 끝
        t.end_fill()
    else :
        t.write("0~8사이 수 입력")

    #반복을 위해 그림판 리셋
    t.reset()
