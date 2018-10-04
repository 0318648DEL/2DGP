import random
from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH,KPU_HEIGHT)

background = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

size = 20
points = [(random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)) for i in range(size)]

def move_left_up(x1, y1,x2,y2):
    move_x=abs(x1-x2)/32
    move_y=abs(y1-y2)/32
    curr_x=x1
    curr_y=y1
    frame=0
    while curr_x>x2 and curr_y<y2:
        clear_canvas_now()
        background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(100*frame,0,100,100,curr_x,curr_y)
        update_canvas()
        frame=(frame+1)%8
        curr_x-=move_x
        curr_y+=move_y
        delay(0.05)

def move_left_down(x1, y1,x2,y2):
    move_x = abs(x1 - x2) / 32
    move_y = abs(y1 - y2) / 32
    curr_x = x1
    curr_y = y1
    frame = 0
    while curr_x > x2 and curr_y > y2:
        clear_canvas_now()
        background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(100 * frame, 0, 100, 100, curr_x, curr_y)
        update_canvas()
        frame = (frame + 1) % 8
        curr_x -= move_x
        curr_y -= move_y
        delay(0.05)

def move_right_up(x1, y1,x2,y2):
    move_x = abs(x1 - x2) / 32
    move_y = abs(y1 - y2) / 32
    curr_x = x1
    curr_y = y1
    frame = 0
    while curr_x < x2 and curr_y < y2:
        clear_canvas_now()
        background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(100 * frame, 100, 100, 100, curr_x, curr_y)
        update_canvas()
        frame = (frame + 1) % 8
        curr_x += move_x
        curr_y += move_y
        delay(0.05)

def move_right_down(x1, y1,x2,y2):
    move_x = abs(x1 - x2) / 32
    move_y = abs(y1 - y2) / 32
    curr_x = x1
    curr_y = y1
    frame = 0
    while curr_x < x2 and curr_y > y2:
        clear_canvas_now()
        background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(100 * frame, 100, 100, 100, curr_x, curr_y)
        update_canvas()
        frame = (frame + 1) % 8
        curr_x += move_x
        curr_y -= move_y
        delay(0.05)

def char_move():
    count=0
    while count<size:
        if points[count][0]>points[(count+1)%size][0] and points[count][1]<points[(count+1)%size][1]:
            move_left_up(points[count][0],points[count][1],points[(count+1)%size][0],points[(count+1)%size][1])
        elif points[count][0]>points[(count+1)%size][0] and points[count][1]>points[(count+1)%size][1]:
            move_left_down(points[count][0],points[count][1],points[(count+1)%size][0],points[(count+1)%size][1])
        elif points[count][0]<points[(count+1)%size][0] and points[count][1]<points[(count+1)%size][1]:
            move_right_up(points[count][0],points[count][1],points[(count+1)%size][0],points[(count+1)%size][1])
        elif points[count][0]<points[(count+1)%size][0] and points[count][1]>points[(count+1)%size][1]:
            move_right_down(points[count][0],points[count][1],points[(count+1)%size][0],points[(count+1)%size][1])
        count += 1

while True:
    char_move()

close_canvas()






