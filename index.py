#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 00:55:23 2025

@author: tolgabal
"""

import turtle
import random

main_screen = turtle.Screen()
main_screen.bgpic("bgpic.gif")
main_screen.screensize(600,338)
main_screen.setup(600,338)
main_screen.addshape("turtlepic.gif")

turtle_turtle = turtle.Turtle()
turtle_turtle.shape("turtlepic.gif")
turtle_turtle.penup()

turtle_writer = turtle.Turtle()
turtle_writer.hideturtle()
turtle_writer.penup()
turtle_writer.color("red")

turtle_counter = turtle.Turtle()
turtle_counter.penup()
turtle_counter.hideturtle()

score = 0
counterVar = 16

def scoreboard_writer(score):
    turtle_writer.clear()
    turtle_writer.goto(-40,128)
    turtle_writer.write("Score: {}".format(score), font=("helvetica", 18, "bold"))

def turtle_clicker(x,y):
    global score
    score +=1
    scoreboard_writer(score)
    
def counter():
    global counterVar
    turtle_counter.clear()
    turtle_counter.goto(-10,98)
    counterVar -= 1
    turtle_counter.write(counterVar, font=("helvetica", 18, "bold"))
    main_screen.ontimer(counter, 1000)
    
def turtle_teleport():
    xPlane = random.randint(-300, 300)
    yPlane = random.randint(-169, 169)
    turtle_turtle.hideturtle()
    turtle_turtle.goto(xPlane,yPlane)
    turtle_turtle.showturtle()
    
    main_screen.ontimer(turtle_teleport, 700)
    
turtle_teleport()
counter()
scoreboard_writer(score)
turtle_turtle.onclick(turtle_clicker)


turtle.mainloop()