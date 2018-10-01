from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    # fill here
    global running
    global x,y
    global move_x,move_y
    global cursor_x,cursor_y
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running=False
        elif event.type==SDL_MOUSEMOTION:
            cursor_x,cursor_y=event.x,KPU_HEIGHT-1-event.y
        elif event.type==SDL_MOUSEBUTTONDOWN:
            move_x=cursor_x
            move_y=cursor_y
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            running=False


# fill here
open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor=load_image("hand_arrow.png")

running = True
dir=0
pos=0
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
move_x,move_y=KPU_WIDTH // 2, KPU_HEIGHT // 2
cursor_x,cursor_y=KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.draw_now(cursor_x,cursor_y)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)
    handle_events()

close_canvas()




