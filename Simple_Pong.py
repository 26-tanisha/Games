#Creating a Simple Pong game using Python 3

import turtle #allows to do basic grapic and gaming for begineers (pre-installed)
wn = turtle.Screen() #create window for game 
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width = 800, height =600)
wn.tracer(0) #stops the window from updating, helps to speed up the preocess

#Paddle 1
pad_1 = turtle.Turtle() #creating object
pad_1.speed(0) #speed of animation = max
pad_1.shape("square")
pad_1.color("white")
pad_1.shapesize(5.5,1)
pad_1.penup()
pad_1.goto(-350,0)
#Paddle 2
pad_2 = turtle.Turtle() #creating object
pad_2.speed(0) #speed of animation = max
pad_2.shape("square")
pad_2.color("white")
pad_2.shapesize(5.5,1)
pad_2.penup()
pad_2.goto(350,0)
#Ball
ball = turtle.Turtle() #creating object
ball.speed(0) #speed of animation = max
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

#Main game loop
while True:
    wn.update()  #everytime loop reuns, the game window is updated 
