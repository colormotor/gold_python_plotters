import numpy as np
from py5canvas import canvas
from PIL import Image
# Note that this example will require OpenCV to be installed
# By default, use webcam as video input
#video = canvas.VideoInput(size=(32, 32))
# Or use a video file
video = canvas.VideoInput(name='images/fingers.mov', size=(32,32))
buf = np.zeros(video.size)
# Also image input is valid
img = Image.open('./images/spock.jpg').resize((32,32))

def setup():
    create_canvas(512, 512)
    set_color_scale(1.0)
    frame_rate(30)

def draw():
    global buf # We modify the global buf variable here
    background(0)
    # Scale to fill screen
    scale(height/video.size[1])
    # Get current video frame, average RGB channels
    # and scale to [0,1] range (from [0,255])
    img = video.read() # Comment this line to use image input
    target = np.mean(img, axis=-1)/255
    # smooth transition between frames
    buf = buf + (target - buf)*0.1
    #image(buf)
    # loop through pixels and draw something
    no_fill()
    stroke(1)
    stroke_weight(0.1)


    for i in range(buf.shape[0]):
        begin_shape()
        for j in range(buf.shape[1]):
            curve_vertex(j, i-buf[i,j]*10)
        end_shape(False)
