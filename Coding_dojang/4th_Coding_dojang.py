# NOTE : 1차원 평면에 있는 점들을 입력받아 거리가 가장 짧은 두 점을 추출

def distance():

    poi = list(map(int, input('점들의 좌표를 입력해 주세요. : ').split(' ')))
    min_dist = 10000000
    min_dist_ind = [0, 0]

    for o_rep in range(len(poi)):

        for i_rep in range(1, len(poi)):

            if poi[i_rep] != poi[o_rep]:
                cal_dist = abs(poi[o_rep] - poi[i_rep])

                if cal_dist <= min_dist:
                    min_dist = cal_dist
                    min_dist_ind[0] = poi[o_rep]
                    min_dist_ind[1] = poi[i_rep]


                print('|{} - {}| = {}'.format(poi[o_rep], poi[i_rep], cal_dist))

            else:
                pass

    return sorted(min_dist_ind)

if __name__ == '__main__':
    print(distance())