from pico2d import*

open_canvas()
character = load_image('characters.gif')

x = 0
frame = 0


def plus():
    frame = 0
    for a in range(0,3):
        clear_canvas()
        character.clip_draw(frame * 20 + 321, 400, 20, 80, x, 90)
        update_canvas()
        frame = (frame + 1) % 3
        delay(0.1)
        get_events()

def minus():
    frame = 1
    clear_canvas()
    character.clip_draw(frame * 20 + 321, 400, 20, 80, x, 90)
    update_canvas()
    delay(0.1)
    get_events()


for x in range (0, 800, 4):
    plus()
    minus()

close_canvas()
