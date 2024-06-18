#!/usr/bin/env python3
import numpy as np

def setup():
    create_canvas(512, 512)

def draw():
    c = sketch.canvas
    background(0)
    c.stroke_weight(2)
    c.stroke(255)
    c.no_fill()
    n_frames = 60
    frame_index = frame_count % n_frames
    phase = (np.pi*2)/n_frames * frame_index
    for y in np.linspace(0, 1, 63)[1:-1]: # Loop 0-1 skipping first and last row (
        c.begin_shape()
        for x in np.linspace(0, 1, 100):
            c.vertex(x*c.width, y*c.height +
                     np.sin(x*np.pi*4 + phase + y*7)*np.cos(y*np.pi*7 + x*5.2)*20)
        c.end_shape()
