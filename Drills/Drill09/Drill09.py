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