#!/usr/bin/env python3
from py5canvas import canvas
import numpy as np

# For this to work you will need to `pip install perlin-noise`
from perlin_noise import PerlinNoise

noise = PerlinNoise()

def setup():
    create_canvas(512, 512)
    set_color_scale(1.0)
    sketch.canvas.tension = 0.5

def draw():
    background(1)
    translate(width/2, height/2)
    stroke(0)
    no_fill()

    for r1 in np.linspace(10, 200, 30):
        begin_shape()
        for t in np.linspace(0, np.pi*2, 20)[:-1]:
            r = r1 + 10 + noise(t*10 + frame_count/100 + r1/100)*50
            curve_vertex(np.cos(t)*r, np.sin(t)*r)
        end_shape(close=True)
