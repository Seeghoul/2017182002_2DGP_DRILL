from pico2d import *
import math
math.sin(270/360*2*math.pi)
-1.0
math.cos(270)

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
while True:
    while (x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x = x+2
        delay(0.01)

    while (y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(800,y)
        y = y+2
        delay(0.01)

    while (x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,600)
        x= x-2
        delay(0.01)
    while (y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0,y)
        y= y-2
        delay(0.01)

    

                   

