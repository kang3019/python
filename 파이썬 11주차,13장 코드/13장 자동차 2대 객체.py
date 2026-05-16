from turtle import *
class Car :
    def __init__(self,speed,color,fname):
        self.speed = speed
        self.color = color
        self.turtle = Turtle()
        self.turtle.shape(fname)


    def drive(self):
        self.turtle.forward(self.speed)


    def left_turn(self):
        self.turtle.left(90)



register_shape("car1.gif")
register_shape("car2.gif")

myCar = Car(200,"blue","car1.gif")
yourCar = Car(200,"red","car2.gif")
for i in range(2):
    myCar.drive()
    myCar.left_turn()




for i in range(2):
    yourCar.drive()
    yourCar.left_turn()
