from pico2d import *
import math

open_canvas()
grass=load_image('grass.png')
char=load_image('character.png')

x=400
y=90
while(1):
    clear_canvas_now()
    grass.draw_now(400,30)
    x=400
    y=90
    r=0
    while(r<6.3):
        clear_canvas_now()
        grass.draw_now(400,30)
        x=400-(math.sin(r)*250)
        y=340-(math.cos(r)*250)
        char.draw_now(x,y)
        r=r+0.1
        delay(0.05)
    while(x<780):
        clear_canvas_now()
        grass.draw_now(400,30)
        char.draw_now(x,y)
        x=x+2
        delay(0.01)
    while(y<580):
        clear_canvas_now()
        grass.draw_now(400,30)
        char.draw_now(x,y)
        y=y+2
        delay(0.01)
    while(x>20):
        clear_canvas_now()
        grass.draw_now(400,30)
        char.draw_now(x,y)
        x=x-2
        delay(0.01)
    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        char.draw_now(x,y)
        y=y-2
        delay(0.01)
    while(x<=400):
        clear_canvas_now()
        grass.draw_now(400,30)
        char.draw_now(x,y)
        x=x+2
        delay(0.01)