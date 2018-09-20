from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    # fill here
    global running
    global x,y
    global move_x,move_y
    global dir, pos
    global go_x,go_y
    global cursor_x,cursor_y
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running=False
        elif event.type==SDL_MOUSEMOTION:
            cursor_x,cursor_y=event.x,KPU_HEIGHT-1-event.y
        elif event.type==SDL_MOUSEBUTTONDOWN:
            move_x=event.x
            move_y=KPU_HEIGHT-1-event.y
            move_dir(event.x,event.y,move_x,move_y,dir,pos,go_x,go_y)
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            running=False


# fill here
open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor=load_image("hand_arrow.png")

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
move_x,move_y=KPU_WIDTH // 2, KPU_HEIGHT // 2
go_x,go_y=KPU_WIDTH // 2, KPU_HEIGHT // 2
cursor_x,cursor_y=KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dir=0
pos=3
hide_cursor()

def move_dir(x,y,mx,my, dir , pos, go_x,go_y):
    if mx>=x and my>=y:
        dir=1
        pos=1
    elif mx<=x and my>=y:
        dir=-1
        pos=0
    elif mx>=x and my<=y:
        dir=2
        pos=1
    elif mx<=x and my<=y:
        dir=-2
        pos=0
    go_x=abs(mx-x)/32
    go_y=abs(my-y)/32

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.draw_now(cursor_x,cursor_y)
    character.clip_draw(frame * 100, 100 * pos, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.02)
    handle_events()
    if dir==1:
        x+=go_x
        y+=go_y
    elif dir==-1:
        x-=go_x
        y+=go_y
    elif dir==2:
        x+=go_x
        y-=go_y
    elif dir==-2:
        x-=go_x
        y-=go_y

close_canvas()




