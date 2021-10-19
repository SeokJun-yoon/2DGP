from pico2d import *
import random
from player import Mario
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
Grass = load_image('res/grass.png')
Background = load_image('res/Background.png')
mario = Mario()

while running:
    handle_events()

    # Game logic
    mario.update()

    # Game drawing
    clear_canvas()
    Grass.draw(75,75,150,150)
    Background.draw(X/2,475,X,650)
    mario.draw()


    update_canvas()

    delay(0.1)


close_canvas()
