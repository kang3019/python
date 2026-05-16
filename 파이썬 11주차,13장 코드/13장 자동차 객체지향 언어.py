from turtle import *
class Car :
    def __init__(self,speed,color,model):
        self.speed = speed
        self.color = color
        self.model = model
        self.turtle = Turtle()
        self.turtle.shape("car1.gif")


    def drive(self):
        self.turtle.forward(self.speed)


    def left_turn(self):
        self.turtle.left(90)



register_shape("car1.gif")

myCar = Car(200,"blue","E-Class")
for i in range(100):
    myCar.drive()
    myCar.left_turn()
