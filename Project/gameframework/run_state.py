from pico2d import *
import game_framework
import title_state

class BackGround:
    def __init__(self):
        self.image = load_image('..\sprites\Tiles.png')

    def draw(self):
        run = 0


class Mario:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('..\sprites\mario.png')

    def update(self):
        self.frame = (self.frame +1) % 3
        self.x += self.dir * 1
        if self.x > 800:
            self.x = 800
            self.dir = -1
        if self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*20 + 100, 100, 100, 100, self.x, self.y)
        if self.dir == -1:
            self.image.clip_draw(self.frame*20 + 100, 0, 100, 100, self.x, self.y)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)

mario = None
background = None

def enter():
    global mario, background
    mario = Mario()
    background = BackGround()

def exit():
    global mario, background
    del mario
    del background

def update():
    mario.update()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    mario.draw()
    background.draw()

def pause():
    pass
def resume():
    pass

open_canvas()

enter()

close_canvas()