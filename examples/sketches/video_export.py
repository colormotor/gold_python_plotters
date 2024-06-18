''' Simple example showing how to create and export
a video loop'''

import imgui

num_frames = 150

def setup():
    create_canvas(512, 512)
    set_color_scale(1.0)
    frame_rate(30)

def gui():
    if imgui.button('Save video'):
        path = sketch.save_file_dialog('mp4')
        if path:
            sketch.grab_movie(path, num_frames)

def draw():
    background(0.0)
    t = frame_count / num_frames
    identity()
    translate(width/2, height/2)
    rotate_deg(t*360)
    fill(1.0)
    circle([200, 0], 20)
