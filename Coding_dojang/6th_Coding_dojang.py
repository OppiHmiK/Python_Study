# -*- coding : utf-8 -*-
# NOTE : KDA를 입력받아 mvp인 플레이어 추출

player_name = ['a1', 'a2', 'a3', 'a4', 'a5',
               'b1', 'b2', 'b3', 'b4', 'b5' ]
player_score = {}

for rep in player_name:
    kda = list(map(int, input('당신의 KDA를 입력하십시오. : ').split(' ')))
    score = (kda[0] * 2 + kda[2]) / kda[1]
    player_score[rep] = score

for rep in range(len(player_score)):

    if list(player_score.values())[rep] == max(player_score.values()):
        mvp = list(player_score.keys())[rep]
        print('MVP : ', mvp)
