import random
from pico2d import *
import game_world
import game_framework

class Ball:

    def __init__(self):
        self.canvas_width=get_canvas_width()
        self.canvas_height=get_canvas_height()
        self.image = load_image('ball21x21.png')

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def set_background(self,bg):
        self.bg = bg
        self.x, self.y = random.randint(300, self.bg.w - 300), random.randint(0, self.bg.h - 1)

    def draw(self):
        cbx,cby=self.x-self.bg.window_left,self.y-self.bg.window_bottom
        self.image.draw(cbx,cby)

    def update(self):
        pass

