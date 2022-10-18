import pico2d
import run_state
import title_state

pico2d.open_canvas()

states = [title_state, run_state]

for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
    state.exit()

pico2d.close_canvas()