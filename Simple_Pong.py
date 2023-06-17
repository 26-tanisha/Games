#Creating a Simple Pong game using Python 3

import turtle #allows to do basic grapic and gaming for begineers (pre-installed)
wn = turtle.Screen() #create window for game 
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width = 800, height =600)
wn.tracer(0) #stops the window from updating, helps to speed up the preocess



#Main game loop
while True:
    wn.update()  #everytime loop reuns, the game window is updated 