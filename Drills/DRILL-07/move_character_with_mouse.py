from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
handX = random.randrange(0, KPU_WIDTH)
handY = random.randrange(0, KPU_HEIGHT)

def handle_events():
    global running
    global x, y, randX, randY
    events=get_events()

    for event in events:
        if event.type ==SDL_QUIT:
            running = False
        #elif event.type==SDL_MOUSEMOTION:
        #    x, y = event.x, KPU_HEIGHT-1-event.y
        elif event.type==SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            running = False
    pass

open_canvas(KPU_WIDTH,KPU_HEIGHT)

# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2

dir = 0
index = 0
frame = 0
# hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    hand.draw(handX,handY)
    if x < handX:
        dirX = +1
        index = 1
    elif x > handX:
        dirX = -1
        index = 0
    else:
        dirX = 0

    if y < handY:
        dirY = +1
    elif y>handY:
        dirY = -1
    else:
        dirY = 0

    character.clip_draw(frame * 100, 100 * index, 100, 100, x, y)

    if dirX == 0 and dirY == 0:
        handX = random.randrange(0, KPU_WIDTH)
        handY = random.randrange(0, KPU_HEIGHT)

    x += dirX
    y += dirY

    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()