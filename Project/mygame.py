import game_framework
import pico2d
import title_state
import main_state

pico2d.open_canvas(1280, 720)
game_framework.run(title_state)
pico2d.close_canvas()