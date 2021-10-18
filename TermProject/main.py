from pico2d import *

frame = 0
index = 0
dir = 0  # -1 left, +1 right

x=50
y=200
open_canvas(1000,800)
def handle_events():
    global running
    global dir
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1



MarioIdle = load_image('res/MarioIdle.png')
MarioRun = load_image('res/MarioRun.png')
Grass = load_image('res/grass.png')
running = True

while running:
    clear_canvas()
    Grass.draw(0,50,2000,200)
    # left, bottom, img.넓이 , 높이, x위치, y위치 , x사이즈, y사이즈
    MarioIdle.clip_draw(frame * 210, index * 290, 210, 290,x,y,100,140)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 3
    x += dir * 5
    delay(0.1)


close_canvas()
