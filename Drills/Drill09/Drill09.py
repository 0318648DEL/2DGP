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

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

ball_rand=random.randint(0,20)
bigBalls=[Ball41() for i in range(ball_rand)]
smallBalls=[Ball21() for i in range(20-ball_rand)]
team=[Boy() for i in range(11)]
grass=Grass()

running=True

while running:
    handle_events()

    for boy in team:
        boy.update()

    for Ball41 in bigBalls:
        Ball41.update()

    for Ball21 in smallBalls:
        Ball21.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()

    for Ball41 in bigBalls:
        Ball41.draw()

    for Ball21 in smallBalls:
        Ball21.draw()

    update_canvas()

    delay(0.05)