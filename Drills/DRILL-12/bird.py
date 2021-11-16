import game_framework
from pico2d import *

import game_world
import random
# Bird Run Speed
PIXEL_PER_METER = (10.0/0.3) # 10 pixel 30cm 기준
MOVE_SPEED_KMPH = 120    # 비둘기가 빠르게 날 때의 속도를 120km/h의 속도로 지정함.
MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0
FRAMES_PER_ACTION = 14

BIRD_WIDTH = 100
BIRD_HEIGHT = 100

class MoveState:

    def enter(bird, event):
        bird.velocity=MOVE_SPEED_PPS*bird.dir


    def exit(bird, event):
        pass


    def do(bird):
        # fill here
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        bird.x = bird.x + bird.velocity * game_framework.frame_time
        bird.x = clamp(60, bird.x, 1600 - 90)
        if bird.x >= 1510 or bird.x<=60:
            bird.dir*=-1
            bird.velocity=MOVE_SPEED_PPS*bird.dir

    @staticmethod
    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_composite_draw(int(bird.frame)*100,
                                           0,
                                           BIRD_WIDTH,
                                           BIRD_HEIGHT,
                                           0,
                                           '',
                                           bird.x,
                                           bird.y,
                                           BIRD_WIDTH,
                                           BIRD_HEIGHT
                                           )
        else:
            bird.image.clip_composite_draw(int(bird.frame)*100,
                                           0,
                                           BIRD_WIDTH,
                                           BIRD_HEIGHT,
                                           0,
                                           'h',
                                           bird.x,
                                           bird.y,
                                           BIRD_WIDTH,
                                           BIRD_HEIGHT
                                           )

next_state_table = {
    MoveState: {},
}

class Bird:

    def __init__(self):
        self.x, self.y = random.randint(0, 1600), random.randint(100,400)
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('bird100x100x14.png')
        # fill here
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = MoveState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        # fill here

    def handle_event(self, event):
        pass
