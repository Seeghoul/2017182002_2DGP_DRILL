from pico2d import *
import game_world
import game_framework

event_name = ['Flying']

#Bird flying speed
PIXEL_PER_METER = (10.0 / 0.3)
FLY_SPEED_KMPH = 20.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 /60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

#Bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 0.8


class Flying:
    def enter(self, event):
        print('ENTER FLYING')
        self.dir = 0

    def exit(self, event):
        print('EXIT FLYING')
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 1600-25)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(int(self.frame)*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(int(self.frame)*100, 100, 100, 100, self.x, self.y)

class Bird:
    def __init__(self):
        self.x, self.y = 100, 70
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        Bird.image = load_image('bird_animation.png')

        self.event_que = []
        self.cur_state = Flying
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)

    def draw(self):
        self.cur_state.draw(self)

