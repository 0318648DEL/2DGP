from pico2d import *
import random

class Ball21:
    def __init__(self):
        self.x,self.y=random.randint(100,700),random.randint(100,500)
        self.image=load_image('ball21x21.png')

    def update(self):
        if(self.y >= 70):
            self.y -= 5

    def draw(self):
        self.image.draw(self.x,self.y)

class Ball41:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(100, 500)
        self.image = load_image('ball41x41.png')

    def update(self):
        if (self.y >= 80):
            self.y -= 5

    def draw(self):
        self.image.draw(self.x, self.y)

class Grass:
    def __init__(self):
        self.image=load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y=random.randint(100,700),90
        self.frame=random.randint(0,7)
        self.image=load_image('run_animation.png')

    def update(self):
        self.frame=(self.frame+1)%8
        self.x+=5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)