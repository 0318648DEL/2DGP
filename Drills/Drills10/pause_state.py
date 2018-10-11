from pico2d import *

import game_framework
import title_state
import main_state

name = "PauseState"

paused = None
grass = None
boy = None

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Pause:
    def __init__(self):
        self.image=load_image('pause.png')

    def draw(self):
        self.image.draw(400,300)

def enter():
    global paused,boy,grass
    paused=Pause()
    boy=main_state.Boy()
    grass=Grass()

def exit():
    global paused
    del(paused)

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()

def update():
    pass

def draw():
    clear_canvas()
    grass.draw()
    main_state.boy.draw()
    update_canvas()
    delay(0.5)

    clear_canvas()
    grass.draw()
    main_state.boy.draw()
    paused.draw()
    update_canvas()
    delay(0.5)