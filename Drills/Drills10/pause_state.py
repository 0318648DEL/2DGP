from pico2d import *

import game_framework
import title_state

name = "PauseState"

paused = None

class Pause:
    def __init__(self):
        self.image=load_image('pause.png')

    def draw(self):
        self.image.draw(400,300)

def enter():
    global paused
    paused=Pause()

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
    paused.draw()
    update_canvas()