#사용자에게 3~6중 입력받아 해당 다각형 그리기
import turtle as t

t.shape()


#사용자에게 입력받기
n = int(t.textinput("","몇각형을 그릴까요?"))

#해당 다각형의 한변의 각 구하기
angle = 360/n

#해당 다각형 그릴 곳으로 이동
t.up()
t.goto(-50,-50)
t.down()

#삼각형~육각형 그리기
if n == 3 :
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
elif n ==4 :
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
elif n ==5 :
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    
elif n ==6 :
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    t.fd(100)
    t.left(angle)
    
else :
    t.write("3~6만 가능합니다.")

t.done()
