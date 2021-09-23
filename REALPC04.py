#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle,random
panel=turtle.Screen()
panel.setup
uno=turtle.Turtle()
dos=turtle.Turtle()
dos.speed(100000)
uno.speed(100000)
RGBcolorpalette=(("black"),("blue"),("yellow"),("red"))
for i in range(5): #used so that turtle will repeatedly move after picking up pen
    dos.penup()
    dos.goto(random.randint(-300,300),random.randint(-300,300))
    dos.pendown()
    dos.color((random.choice(RGBcolorpalette)))
    for i in range(1,100): #repeats the following steps 100 times
        dos.fd(200)
        dos.rt(90)
        dos.fd(200)
        dos.rt(90)
        dos.rt(5)
for i in range(5): #same code, used for second turtle
    uno.penup() 
    uno.goto(random.randint(-300,300),random.randint(-300,300)) #random place
    uno.pendown()
    uno.color((random.choice(RGBcolorpalette))) #chooses a random color 
    for i in range(1,100): 
        uno.fd(200)
        uno.rt(90)
        uno.fd(200)
        uno.rt(90)
        uno.rt(5)
