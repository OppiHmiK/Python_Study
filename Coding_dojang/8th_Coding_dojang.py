# -*- coding: utf-8 -*-
# NOTE : 삽입 정렬

def insertion_sort():
    arr = list(map(int, input('자료를 입력해 주세요. : ').split(' ')))

    for o_rep in range(1, len(arr)):

        for i_rep in range(o_rep):
            if arr[o_rep] == arr[i_rep]:
                pass

            else:
                if arr[o_rep] < arr[i_rep]:
                    arr[o_rep], arr[i_rep] = arr[i_rep], arr[o_rep]

                    print(arr)


    return arr

print(insertion_sort())
