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
ball.dx=0.3 #the ball moves by 0.3 pixel x
ball.dy=0.3

#Function for movement
def pad_1_up():
    y = pad_1.ycor() #from turtle module, returns the y coordinates
    y += 20
    pad_1.sety(y) #set ycor to new value of y
    
def pad_1_down():
    y = pad_1.ycor() #from turtle module, returns the y coordinates
    y -= 20
    pad_1.sety(y) #set ycor to new value of y
    
def pad_2_up():
    y = pad_2.ycor() #from turtle module, returns the y coordinates
    y += 20
    pad_2.sety(y) #set ycor to new value of y
    
def pad_2_down():
    y = pad_2.ycor() #from turtle module, returns the y coordinates
    y -= 20
    pad_2.sety(y) #set ycor to new value of y

#Keyboard binding
wn.listen() #listen to keyboard commands/inputs
wn.onkeypress(pad_1_up, "w")
wn.onkeypress(pad_1_down, "s")
wn.onkeypress(pad_2_up, "Up")
wn.onkeypress(pad_2_down, "Down")

#Main game loop
while True:
    wn.update()  #everytime loop reuns, the game window is updated 

    
    #Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Border Checking for ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*= -1 #reverse the ball direction (bounce of the ball from boundry)
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*= -1
        
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx*= -1
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx*= -1
    
    #Boundry restriction for paddles
    if pad_1.ycor() > 220:
        pad_1.sety(220) 
        
    if pad_1.ycor() < -220:
        pad_1.sety(-220)
    
    if pad_2.ycor() > 220:
        pad_2.sety(220) 
        
    if pad_2.ycor() < -220:
        pad_2.sety(-220)