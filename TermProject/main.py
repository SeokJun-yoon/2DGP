from pico2d import *
import random
from player import Mario
from ground import Ground
from background import Background
X,Y=512*2,160*5
running = True

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
        mario.handle_event(event)

open_canvas(1000,800)
# Ground = load_image('res/ground.png')
# Background = load_image('res/Background.png')
mario = Mario()
ground = Ground()
background = Background()
while running:
    handle_events()

    # Game logic
    mario.update()

    # Game drawing
    clear_canvas()
    ground.draw()
    background.draw()
    mario.draw()

    update_canvas()

    delay(0.1)


close_canvas()
