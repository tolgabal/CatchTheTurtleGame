# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 00:55:23 2025

@author: tolgabal
"""

import turtle
import random
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return relative_path

main_screen = turtle.Screen()
main_screen.bgpic(resource_path("bgpic.gif"))
main_screen.screensize(600,338)
main_screen.setup(600,338)
main_screen.addshape(resource_path("turtlepic.gif"))
main_screen.addshape(resource_path("endgameturtle.gif"))

turtle_turtle = turtle.Turtle()
turtle_turtle.shape(resource_path("turtlepic.gif"))
turtle_turtle.penup()

turtle_writer = turtle.Turtle()
turtle_writer.hideturtle()
turtle_writer.penup()
turtle_writer.color("red")

turtle_counter = turtle.Turtle()
turtle_counter.penup()
turtle_counter.hideturtle()

turtle_endgame = turtle.Turtle()
turtle_endgame.hideturtle()
turtle_endgame.shape(resource_path("endgameturtle.gif"))

score = 0
total_click = 0
counterVar = 16

def scoreboard_writer():
    global score
    global total_click
    turtle_writer.clear()
    turtle_writer.goto(-100,128)
    turtle_writer.write("Score: " + str(score) + "    Total Try: " + str(total_click), font=("helvetica", 18, "bold"))

def turtle_clicker(x,y):
    global score
    score += 1
    scoreboard_writer()
    
def screen_clicker(x,y):
    global total_click
    total_click += 1
    scoreboard_writer()
    
def counter():
    global counterVar
    if counterVar >0:
        turtle_counter.clear()
        turtle_counter.goto(-10,98)
        counterVar -= 1
        turtle_counter.write(counterVar, font=("helvetica", 18, "bold"))
    if counterVar == 0:
        gameover()
    main_screen.ontimer(counter, 1000)
    
def turtle_teleport():
    global score
    if counterVar > 0:
        xPlane = random.randint(-300, 300)
        yPlane = random.randint(-169, 169)
        turtle_turtle.hideturtle()
        turtle_turtle.goto(xPlane,yPlane)
        turtle_turtle.showturtle()
    main_screen.ontimer(turtle_teleport, 1000-(score*50))
    if counterVar == 0:
        turtle_turtle.hideturtle()
    
def gameover():
    turtle_turtle.hideturtle()
    turtle_counter.goto(-100,0)
    turtle_counter.write("Game Over", font=("helvetica", 36, "bold"))
    turtle_endgame.showturtle()
    
turtle_teleport()
counter()
scoreboard_writer()
turtle_turtle.onclick(turtle_clicker)
main_screen.onclick(screen_clicker)


turtle.mainloop()