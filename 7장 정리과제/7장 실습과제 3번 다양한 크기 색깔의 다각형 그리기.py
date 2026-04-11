import turtle as t
import random as r

def drow(n,length):
    if n > 2  :
        for i in range(n) :            
            t.fd(length)
            t.left(360/n)
    else :
        print("2 이상의 값을 입력해주세요")


while True :
    n = int(input("몇 각형을 그리시겠습니까?"))

    # 랜덤 위치 생성 및 이동
    x = r.randint(-200, 200) 
    y = r.randint(-200, 200)
    t.up()
    t.goto(x, y)
    t.down()

    # 0.0 ~ 1.0 사이의 무작위 값 3개를 RGB 값으로 지정
    t.color(r.random(),r.random(),r.random())

    t.begin_fill()
    drow(n,r.randint(10,100))
    t.end_fill()
   
    
