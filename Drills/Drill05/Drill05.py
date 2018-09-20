from pico2d import *

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def move_left_up(px,py,nx,ny):
    curr_x=px
    curr_y=py
    frame=0
    frame_x=(px-nx)/8
    frame_y=(ny-px)/8
    while curr_x>nx and curr_y<ny:
        clear_canvas_now()
        grass.draw(400,30)
        character.clip_draw(frame*100,100,100,100,curr_x,curr_y)
        update_canvas()
        frame=(frame+1)%8
        curr_x -= frame_x
        curr_y += frame_y
        delay(0.05)
        get_events()


def move_left_down():
    pass

def move_right_up():
    pass

def move_right_down():
    pass

def character_movement():
    data=[[203,535],[132,243],[535,470],[477,203],[715,136],[316,225],[510,92],[692,518],[682,336],[712,349]]
    count=0
    while count<9:
        if data[count][0]>data[count+1][0]and data[count][1]<data[count+1][1]:
            move_left_up(data[count][0],data[count][1],data[count+1][0],data[count+1][1])
        ++count


while True:
    character_movement()


close_canvas()
