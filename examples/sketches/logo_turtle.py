from py5canvas import *
import numpy as np
from py5canvas.turtle import Turtle 

def setup():
    create_canvas(600, 600)
    background(0)
    translate(width/2, height/2)
    t = Turtle()
    for i in range(36):
        t.right(10)
        t.circle(120, steps=11)
    stroke(255, 0, 0)
    no_fill()
    shape(t.paths)

def draw():
    pass

def key_pressed():
    print('saving')
    save_svg('turtle.svg')
    
run()