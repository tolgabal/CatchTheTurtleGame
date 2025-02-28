#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 00:55:23 2025

@author: tolgabal
"""

import turtle

main_screen = turtle.Screen()
main_screen.bgpic("bgpic.gif")
main_screen.screensize(600,338)
main_screen.setup(600,338)
main_screen.addshape("turtlepic.gif")

turtle_turtle = turtle.Turtle()
turtle_turtle.shape("turtlepic.gif")

turtle_writer = turtle.Turtle()
turtle_writer.hideturtle()
turtle_writer.penup()
turtle_writer.color("red")

score = 0

def scoreboard_writer(score):
    turtle_writer.clear()
    turtle_writer.goto(-40,128)
    turtle_writer.write("Score: {}".format(score), font=("helvetica", 18, "bold"))

def turtle_clicker(x,y):
    global score
    score +=1
    scoreboard_writer(score)
    
scoreboard_writer(score)

turtle_turtle.onclick(turtle_clicker)

turtle.mainloop()