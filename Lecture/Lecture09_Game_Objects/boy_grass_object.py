from pico2d import *
import random
running=True

# Game object class here
class Ball():
    def __init__(self):
        self.x, self.y = random.randint(0, 790), 599
        self.image1 = load_image('ball21x21.png')
        self.image2 = load_image('ball41x41.png')
        

    def draw(self):
        self.image1.draw(self.x,self.y)
        self.image2.draw(self.x,self.y)

    def update(self):
        self.y-=5

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas(800,600)

grass=load_image('grass.png')
ball=Ball()
# game main loop code
while running:
    handle_events()
    clear_canvas()
    grass.draw(400, 30)
    balls = [Ball() for i in range(20)]
    for ball in balls:
        ball.draw()
    for ball in balls:
        ball.update()

    update_canvas()

    delay(0.05)
# finalization code