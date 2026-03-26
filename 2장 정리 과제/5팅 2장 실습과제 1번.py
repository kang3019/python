import turtle as t
t.shape("turtle")

bSize1 = int(input("자동차 몸체의 가로 크기는 얼마로 할까요? : "))
bSize2 = int(input("자동차 몸체의 세로 크기는 얼마로 할까요? : "))
bColor = input("자동차 몸체의 색깔을 입력 : ")

sSize1 = int(input("자동차 창문의 가로 크기는 얼마로 할까요? : "))
sSize2 = int(input("자동차 창문의 세로 크기는 얼마로 할까요? : "))           
sColor = input("자동차 창문의 색깔을 입력 : ")

r = int(input("자동차 바퀴의 반지릉을 입력 : "))
cColor = input("자동차 바퀴의 색깔 : ")

# 1. 자동차 몸체 그리기 (빨간색)
t.up()
#펜 올리기
t.goto(-(bSize1/2), -(bSize2/2))
#중앙에 그리기 위해 좌표 설정
t.down()
#펜 내리기
t.fillcolor(bColor)
#채우는 색 빨강
t.begin_fill()
#채우기 시작
t.forward(bSize1)
t.left(90)
t.forward(bSize2)
t.left(90)
t.forward(bSize1)
t.left(90)
t.forward(bSize2)

t.end_fill()
#채우기 끝

# 2. 자동차 상단 그리기 (노란색)
t.up()
t.goto(-(sSize1/2),(bSize2/2))
t.down()
t.fillcolor(sColor)
t.begin_fill()
t.left(90)
t.forward(sSize1)
t.left(90)
t.forward(sSize2)  
t.left(90)
t.forward(sSize1)
t.left(90)
t.forward(sSize2)
t.end_fill()

# 3. 자동차 타이어 그리기 (검정색)
t.up()
t.goto((-(bSize1/4)-r),-(bSize2/2))
t.down()
t.fillcolor(cColor)
t.begin_fill()
t.circle(r)
t.end_fill()

t.up()
t.goto(((bSize1/4)-r),-(bSize2/2))
t.down()
t.fillcolor(cColor)
t.begin_fill()
t.circle(r)
t.end_fill()
