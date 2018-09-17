from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

# fill here
def move_left_up(x1, y1,x2,y2):
    move_x=abs(x1-x2)/32
    move_y=abs(y1-y2)/32
    curr_x=x1
    curr_y=y1
    frame=0
    while curr_x>x2 and curr_y<y2:
        clear_canvas_now()
        grass.draw(400,30)
        character.clip_draw(100*frame,0,100,100,curr_x,curr_y)
        update_canvas()
        frame=(frame+1)%8
        curr_x-=move_x
        curr_y+=move_y
        delay(0.05)
    pass

def move_left_down():
    pass

def move_right_up():
    pass

def move_right_down():
    pass

def char_move():
    count=0
    data=[[203,535],[132,243],[535,470],[477,203],[715,136],[316,225],[510,92],[692,518],[682,336],[712,349]]
    while count<9:
        if data[count][0]>data[count+1][0] and data[count][1]<data[count+1][1]:
            move_left_up(data[count][0],data[count][1],data[count+1][0],data[count+1][1])
    pass

while True:
    char_move()

close_canvas()
