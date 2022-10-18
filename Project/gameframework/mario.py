import pico2d
import game_framework
import title_state
import run_state

pico2d.open_canvas()

game_framework.run(run_state)
pico2d.clear_canvas()