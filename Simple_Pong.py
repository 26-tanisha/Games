#Creating a Simple Pong game using Python 3
import turtle #allows to do basic grapic and gaming for begineers (pre-installed)
wn = turtle.Screen() #create window for game 
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width = 800, height =600)
wn.tracer(0) #stops the window from updating, helps to speed up the preocess

#Scores
score_a = 0
score_b = 0

#Paddle 1
pad_a = turtle.Turtle() #creating object
pad_a.speed(0) #speed of animation = max
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350,0)
#Paddle 2
pad_b = turtle.Turtle() #creating object
pad_b.speed(0) #speed of animation = max
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350,0)
#Ball
ball = turtle.Turtle() #creating object
ball.speed(0) #speed of animation = max
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.3 #the ball moves by 0.3 pixel x
ball.dy=0.3

#Scoring screen
pen = turtle.Turtle()
pen.speed(0) #animation speed
pen.color("white")
pen.penup() #move the pen without it drawing the line
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align = "center", font=("Courier", 16, "bold"))


#Function for movement
def pad_a_up():
    y = pad_a.ycor() #from turtle module, returns the y coordinates
    y += 20
    pad_a.sety(y) #set ycor to new value of y
    
def pad_a_down():
    y = pad_a.ycor() #from turtle module, returns the y coordinates
    y -= 20
    pad_a.sety(y) #set ycor to new value of y
    
def pad_b_up():
    y = pad_b.ycor() #from turtle module, returns the y coordinates
    y += 20
    pad_b.sety(y) #set ycor to new value of y
    
def pad_b_down():
    y = pad_b.ycor() #from turtle module, returns the y coordinates
    y -= 20
    pad_b.sety(y) #set ycor to new value of y

#Keyboard binding
wn.listen() #listen to keyboard commands/inputs
wn.onkeypress(pad_a_up, "w")
wn.onkeypress(pad_a_down, "s")
wn.onkeypress(pad_b_up, "Up")
wn.onkeypress(pad_b_down, "Down")

#Main game loop
while True:
    wn.update()  #everytime loop reuns, the game window is updated 

    #Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Border Checking for ball
    #Top and Bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*= -1 #reverse the ball direction (bounce of the ball from boundry)
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*= -1
        
    
    #Left and Right   
    if ball.xcor() > 350:
        score_a +=1 #increse player a score
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font=("Courier", 16, "bold")) #update score on screen
        ball.goto(0,0)
        ball.dx *=-1
        
    elif ball.xcor() < -350:
        score_b +=1 #increase player b score
        pen.clear() 
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font=("Courier", 16, "bold"))
        ball.goto(0,0)
        ball.dx *=-1
    
    #Boundry restriction for paddles
    if pad_a.ycor() > 220:
        pad_a.sety(220) 
        
    if pad_a.ycor() < -220:
        pad_a.sety(-220)
    
    if pad_b.ycor() > 220:
        pad_b.sety(220) 
        
    if pad_b.ycor() < -220:
        pad_b.sety(-220)
        
    #paddle-ball collision
    if ((ball.xcor() > 340) and (ball.xcor() < 350)) and ((ball.ycor() < pad_b.ycor() + 40) and (ball.ycor() > pad_b.ycor()- 40)):
        ball.setx(340)
        ball.dx *= -1
        
        
    elif ((ball.xcor() < -340) and (ball.xcor() > -350)) and ((ball.ycor() < pad_a.ycor() + 40) and (ball.ycor() > pad_a.ycor()- 40)):
        ball.setx(-340)
        ball.dx *= -1
        
        