from pico2d import *
import random
running = True

frame = 0
index = 0
dir = 0  # -1 left, +1 right

x=50
y=200

class Mario:
    def __init__(self): # 생성자
        self.x = 50
        self.y = 200
        self.frame=0
        self.index=0
        self.speed=0
        self.dir=[1,0]          # -1 left, +1 right

        self.state="Idle"
        self.Idle_image = load_image('res/MarioIdle.png')
        self.Run_image = load_image('res/MarioRun.png')

    def Run(self):
        pass

    def Jump(self):
        pass

    def change_state(self):
        pass

    def draw(self):
        if self.state is "Idle":
            self.Idle_image.clip_draw(self.frame * 210, self.index * 290, 210, 290,self.x,self.y,100,140)
        elif self.state is "Run":
            self.Run_image.clip_draw(self.frame*223,self.index*275,223,275,self.x,self.y,100,120)

    def handle_event(self,e):
            if e.type == SDL_KEYDOWN:
                if e.key == SDLK_RIGHT:
                    self.speed=1
                    self.dir[0]= 1
                    self.state = "Run"
                    self.index=0
                elif e.key == SDLK_LEFT:
                    self.speed=1
                    self.dir[0] = -1
                    self.state = "Run"
                    self.index=1
            elif e.type == SDL_KEYUP:
                if e.key == SDLK_RIGHT:
                    self.speed=0
                    self.state = "Idle"
                elif e.key == SDLK_LEFT:
                    self.speed=0
                    self.state = "Idle"

    def update(self):
        self.frame= (self.frame+1) % 3   # 프레임
        # self.handle_event()
        self.x+=self.dir[0]*self.speed*10


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
mario = Mario()

while running:
    handle_events()

    # Game logic
    mario.update()

    # Game drawing
    clear_canvas()
    Grass.draw(50,50,150,150)
    mario.draw()

    # left, bottom, img.넓이 , 높이, x위치, y위치 , x사이즈, y사이즈
    #MarioIdle.clip_draw(frame * 210, index * 290, 210, 290,x,y,100,140)
    #frame = (frame + 1) % 3
    #x += dir * 5
    update_canvas()

    delay(0.1)


close_canvas()
