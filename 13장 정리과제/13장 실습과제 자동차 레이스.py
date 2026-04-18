from turtle import *
import random as r

#Car 클래스 :  x,y,스피드,이미지 정보를 받아 이미지를 고르고 해당 장소로 이동시킴 
class Car :
    def __init__(self,x,y,speed,fname):
        self.x = x
        self.y = y
        self.speed = speed
        self.turtle = Turtle()
        self.turtle.shape(fname)
        self.turtle.penup()
        self.turtle.goto(self.x,self.y)
      

      
    #drive 메소드 : 거리를 입력받아 해당 팬촉이 이동함
    def drive(self,distance):
        self.turtle.forward(distance)

# 결승선 그리기 함수
def draw_finish_line(x_pos):
    # 펜 설정
    tracer(False) # 화면 업데이트 끄기 (그리기 속도 향상)
    
    pen = Turtle()
    pen.penup()
    
    # 결승선 시작 위치로 이동
    pen.goto(x_pos, 250)
    pen.pendown()
    
    # 결승선 색상 및 두께 설정
    pen.color("black")
    pen.pensize(3)
    
    # 수직선 그리기
    pen.goto(x_pos, -200)
    tracer(True) # 화면 업데이트 켜기
    



#이걸 펜촉 쉐잎으로 저장시킴
register_shape("car1.gif")
register_shape("car2.gif")


car_colors = ["car1.gif","car2.gif"]

car_list = []
draw_finish_line(200)
h = -125
#공백 리스트에 Car 객체를 넣음
for i in range(5) :
    car_list.append(Car(-350,h,r.randint(1,10),r.choice(car_colors)))
    h += 50

finish_list = []

# 순위 출력 전용 Turtle 객체 생성
rank_writer = Turtle()
rank_writer.hideturtle() # Turtle 모양 숨기기
rank_writer.penup()      # 펜을 들고 이동 (선이 그려지지 않도록)
rank_writer.speed(0)     # 최고 속도로 설정

# 순위 기록을 위한 변수 추가
ranking = 1

# finish_list 길이가 5보다 작을 때까지 반복문
while len(finish_list) < 5 :
    
    # 1. 자동차 이동 
    for j in car_list:
        if j not in finish_list:
            j.drive(r.randint(10, 50))

    # 2. 순위 판별 및 기록 
    for car in car_list :
        
        # X좌표가 200보다 크고 finish_list에 없다면
        if car.turtle.xcor() > 200 and car not in finish_list :
            
            # 도착 리스트에 추가 (순위 확정)
            finish_list.append(car)
            
            # 자동차 멈추기 (더 이상 움직이지 않도록 drive(0))
            car.drive(0) 
            
           # [220, car.y] 위치에 등수와 자동차 종류 출력
            rank_writer.goto(220, car.y)
            rank_writer.write(
                f"{ranking}등: {car.turtle.shape()}", 
                align="left", 
                font=("Arial", 12, "bold")
            )
            
            ranking += 1


