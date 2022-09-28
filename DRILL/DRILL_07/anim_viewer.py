from pico2d import*

open_canvas()
character = load_image('characters.gif')

x = 0
frame = 0

for x in range (0, 800, 10):
    clear_canvas()
    character.clip_draw(frame * 20 + 320, 400, 20, 80, x, 90,)
    update_canvas()
    frame = (frame +1) % 3
    delay(0.1)
    get_events()

close_canvas()
