from pico2d import *

# 2.이벤트 정의
# RD, LD, RU, LU = 0, 1, 2, 3 => 버그의 여지가 있음.
RD, LD, RU, LU, TIMER, A = range(6)

# 키 입력 확인을 단순화시켜서 이벤트로 해석
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU,
    (SDL_KEYDOWN, SDLK_a) : A,
    (SDL_KEYUP, SDLK_a) : A
}



#4. 상태 변환 실행 구현 - 큐를 활용


#1. 상태 정의
class IDLE:
    def enter(self, event):    # 상태에 들어갈 때 행하는 액션
        print('enter idle')
        self.dir = 0
        self.timer = 1000
        pass

    def exit(self):     # 상태를 나올 때 행하는 액션, 고개 들기
        print('exit idle')
        pass

    def do(self):       # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)
        pass

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        pass


class RUN:
    def enter(self,event):
        #방향을 결정해야 하는데, 뭘 근거로? 어떤 키가 눌렸는지 판단...
        #키 이벤트 정보가 필요.
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        pass

    def exit(self):
        self.face_dir = self.dir
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)
        pass

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

class SLEEP:
    def enter(self, event):    # 상태에 들어갈 때 행하는 액션
        print('enter sleep')
        pass

    def exit(self):     # 상태를 나올 때 행하는 액션, 고개 들기
        print('exit idle')
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        pass

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           -3.141592/2, '',
                                           self.x + 25, self.y - 25, 100, 100)
        else: # 오른쪽으로 눕히기
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           3.141592/2,'',
                                           self.x - 25, self.y - 25, 100, 100)

class AUTO:
    def enter(self, event):
        if event == A:
            print('enter auto')
            if self.face_dir == 1:
                self.dir +=1
            elif self.face_dir ==-1:
                self.dir -= 1
            if self.x == 0:
                self.self_dir = 1
            elif self.x == 800:
                self.face_dir = -1

    def exit(self):
        print('exit auto')
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)
        pass

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y, 200, 200)
        elif self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y, 200, 200)

#3. 상태 변환 기술
next_state = {
    SLEEP : {RD : RUN, LD : RUN, RU : RUN, LU : RUN, TIMER : SLEEP},
    IDLE : {RU : RUN, LU : RUN, RD : RUN, LD : RUN, TIMER : SLEEP, A : AUTO},
    RUN : {RU : IDLE, LU : IDLE, RD : IDLE, LD : IDLE, A : AUTO},
    AUTO : {A : AUTO, RD : RUN, LD : RUN, RU : RUN, LU : RUN}
}

class Boy:
    def add_event(self, event):
        self.q.insert(0,event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_ESCAPE:
        #             game_framework.quit()
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1


    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = [] # 이벤트 큐 초기화
        self.cur_state = IDLE
        self.cur_state.enter(self, None) # 초기 상태의 엔트리 액션 수행


    def update(self):
        self.cur_state.do(self)

        # 이벤트 확인 후 이벤트가 있다면 이벤트 변환 처리
        if self.q : # 큐에 이벤트가 있으면
            event = self.q.pop()
            self.cur_state.exit(self) # 현재 상태를 나가야되고,
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event) # 다음 상태의 엔트리 액션 수행

        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)


