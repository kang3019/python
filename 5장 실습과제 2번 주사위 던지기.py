#난수 라이브러리 호출
import random as r
#터틀 라이브러리 호출
import turtle as t



screen = t.Screen()
image1 = "dice1.gif"
image2 = "dice2.gif"
image3 = "dice3.gif"
image4 = "dice4.gif"
image5 = "dice5.gif"
image6 = "dice6.gif"

#이미지를 추가한다
screen.addshape(image1)
screen.addshape(image2)
screen.addshape(image3)
screen.addshape(image4)
screen.addshape(image5)
screen.addshape(image6)


#첫번째 거북이 생성
t1 = t.Turtle()

print("주사위 게임을 시작합니다")

#랜덤하게 0~5까지 a에 저장
a = r.randrange(6)

if a == 0 :
    t.shape(image1)
    t1.stamp()
elif a == 1:
    t.shape(image2)
    t1.stamp()
elif a == 2:
    t.shape(image3)
    t1.stamp()
elif a == 3:
    t.shape(image4)
    t1.stamp()
elif a == 4:
    t.shape(image5)
    t1.stamp()
elif a == 5:
    t.shape(image6)
    t1.stamp()
