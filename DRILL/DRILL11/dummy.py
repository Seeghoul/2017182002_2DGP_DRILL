# # class Star:  #클래스의 역할은 함수 또는 변수를 묶는다. 그룹 이름으로.
# #     x = 100
# #     def change():
# #         x = 200
# #         print ('x is',x)
# #
# # print(Star.x) #Star 클래스. x는 클래스 변수
# # Star.change() # 클래스 함수 호출
# #
# # star = Star() # 비록 객체 생성용이 아니더라도 객체는 만들어진다
# # star.change()
#
#
#
# class Player:
#     def __init__(tttt):
#         tttt.x = 100
#
#     def where(ssss):
#         print(ssss.x)
#
# player = Player()
# player.where()
#
# # Player.where() # 클래스의 함수 호출
# Player.where(player)
#
# player.where() # 객체 함수 호출 == Player.where(player)


#
# table = {
#     'SLEEP' : {'HIT'  : 'WAKE'},
#     'WAKE'  : {'TIMER 10' : 'SLEEP'}
# }
#
# cur_state = 'SLEEP'
# event = 'HIT'
# next_state = table[cur_state][event]
# print(table[cur_state]['HIT'])
# print(table['WAKE']['TIMER10'])

