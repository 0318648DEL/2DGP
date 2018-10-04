import random
from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH,KPU_HEIGHT)

background = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

size = 10
frame = 0
points = [(random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)) for i in range(size)]

def move_left_up(x1, y1,f):
    curr_x=x1
    curr_y=y1
    clear_canvas_now()
    background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(100*f,0,100,100,curr_x,curr_y)
    update_canvas()
    delay(0.05)

def move_left_down(x1, y1,f):
    curr_x = x1
    curr_y = y1
    clear_canvas_now()
    background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(100 * f, 0, 100, 100, curr_x, curr_y)
    update_canvas()
    delay(0.05)

def move_right_up(x1, y1,f):
    curr_x = x1
    curr_y = y1
    clear_canvas_now()
    background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(100 * f, 100, 100, 100, curr_x, curr_y)
    update_canvas()
    delay(0.05)

def move_right_down(x1, y1,f):
    curr_x = x1
    curr_y = y1
    clear_canvas_now()
    background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(100 * f, 100, 100, 100, curr_x, curr_y)
    update_canvas()
    delay(0.05)

def draw_curve_10p_connect(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,f):

    # draw p1-p2
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p10[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p2[0] + (t ** 3 - t ** 2) * p3[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p10[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p2[1] + (t ** 3 - t ** 2) * p3[1]) / 2
        if p1[0]>p2[0] and p1[1]<p2[1]:
            move_left_up(x,y,f)
        elif p1[0]>p2[0] and p1[1]>p2[1]:
            move_left_down(x,y,f)
        elif p1[0]<p2[0] and p1[1]<p2[1]:
            move_right_up(x,y,f)
        elif p1[0]<p2[0] and p1[1]>p2[1]:
            move_right_down(x,y,f)
        f = (f + 1) % 8

    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        if p2[0]>p3[0] and p2[1]<p3[1]:
            move_left_up(x,y,f)
        elif p2[0]>p3[0] and p2[1]>p3[1]:
            move_left_down(x,y,f)
        elif p2[0]<p3[0] and p2[1]<p3[1]:
            move_right_up(x,y,f)
        elif p2[0]<p3[0] and p2[1]>p3[1]:
            move_right_down(x,y,f)
        f = (f + 1) % 8

    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p5[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p5[1]) / 2
        if p3[0]>p4[0] and p3[1]<p4[1]:
            move_left_up(x,y,f)
        elif p3[0]>p4[0] and p3[1]>p4[1]:
            move_left_down(x,y,f)
        elif p3[0]<p4[0] and p3[1]<p4[1]:
            move_right_up(x,y,f)
        elif p3[0]<p4[0] and p3[1]>p4[1]:
            move_right_down(x,y,f)
        f = (f + 1) % 8


    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p5[0] + (t ** 3 - t ** 2) * p6[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p5[1] + (t ** 3 - t ** 2) * p6[1]) / 2
        if p4[0]>p5[0] and p4[1]<p5[1]:
            move_left_up(x,y,f)
        elif p4[0]>p5[0] and p4[1]>p5[1]:
            move_left_down(x,y,f)
        elif p4[0]<p5[0] and p4[1]<p5[1]:
            move_right_up(x,y,f)
        elif p4[0]<p5[0] and p4[1]>p5[1]:
            move_right_down(x,y,f)
        f = (f + 1) % 8


    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p6[0] + (t ** 3 - t ** 2) * p7[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p6[1] + (t ** 3 - t ** 2) * p7[1]) / 2
        if p5[0]>p6[0] and p5[1]<p6[1]:
            move_left_up(x,y,f)
        elif p5[0]>p6[0] and p5[1]>p6[1]:
            move_left_down(x,y,f)
        elif p5[0]<p6[0] and p5[1]<p6[1]:
            move_right_up(x,y,f)
        elif p5[0]<p6[0] and p5[1]>p6[1]:
            move_right_down(x,y,f)
        f = (f + 1) % 8


    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p5[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p7[0] + (t ** 3 - t ** 2) * p8[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p5[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p7[1] + (t ** 3 - t ** 2) * p8[1]) / 2
        if p6[0]>p7[0] and p6[1]<p7[1]:
            move_left_up(x,y,f)
        elif p6[0]>p7[0] and p6[1]>p7[1]:
            move_left_down(x,y,f)
        elif p6[0]<p7[0] and p6[1]<p7[1]:
            move_right_up(x,y,f)
        elif p6[0]<p7[0] and p6[1]>p7[1]:
            move_right_down(x,y,f)
        f = (f + 1) % 8


    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p6[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p8[0] + (t ** 3 - t ** 2) * p9[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p6[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p8[1] + (t ** 3 - t ** 2) * p9[1]) / 2
        if p7[0]>p8[0] and p7[1]<p8[1]:
            move_left_up(x,y,f)
        elif p7[0]>p8[0] and p7[1]>p8[1]:
            move_left_down(x,y,f)
        elif p7[0]<p8[0] and p7[1]<p8[1]:
            move_right_up(x,y,f)
        elif p7[0]<p8[0] and p7[1]>p8[1]:
            move_right_down(x,y,f)
        f = (f + 1) % 8


    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p7[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p9[0] + (t ** 3 - t ** 2) * p10[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p7[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p9[1] + (t ** 3 - t ** 2) * p10[1]) / 2
        if p8[0]>p9[0] and p8[1]<p9[1]:
            move_left_up(x,y,f)
        elif p8[0]>p9[0] and p8[1]>p9[1]:
            move_left_down(x,y,f)
        elif p8[0]<p9[0] and p8[1]<p9[1]:
            move_right_up(x,y,f)
        elif p8[0]<p9[0] and p8[1]>p9[1]:
            move_right_down(x,y,f)
        f = (f + 1) % 8


    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p8[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p10[0] + (t ** 3 - t ** 2) * p1[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p8[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p10[1] + (t ** 3 - t ** 2) * p1[1]) / 2
        if p9[0]>p10[0] and p9[1]<p10[1]:
            move_left_up(x,y,f)
        elif p9[0]>p10[0] and p9[1]>p10[1]:
            move_left_down(x,y,f)
        elif p9[0]<p10[0] and p9[1]<p10[1]:
            move_right_up(x,y,f)
        elif p9[0]<p10[0] and p9[1]>p10[1]:
            move_right_down(x,y,f)
        f = (f + 1) % 8


    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p9[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p1[0] + (t ** 3 - t ** 2) * p2[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p9[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p1[1] + (t ** 3 - t ** 2) * p2[1]) / 2
        if p10[0]>p1[0] and p10[1]<p1[1]:
            move_left_up(x,y,f)
        elif p10[0]>p1[0] and p10[1]>p1[1]:
            move_left_down(x,y,f)
        elif p10[0]<p1[0] and p10[1]<p1[1]:
            move_right_up(x,y,f)
        elif p10[0]<p1[0] and p10[1]>p1[1]:
            move_right_down(x,y,f)
        f = (f + 1) % 8


while True:
    draw_curve_10p_connect(points[0], points[1], points[2], points[3], points[4], points[5], points[6], points[7],
                           points[8], points[9], frame)

close_canvas()