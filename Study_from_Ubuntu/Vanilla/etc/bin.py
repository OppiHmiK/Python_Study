def solution(N):

    bin_N = bin(N)
    bin_N = bin_N[2:len(bin_N)]
    cnt = 0

    for rep in range(0, len(bin_N)):
        if bin_N[rep] == '0':
            cnt += 1

        if bin_N[rep:len(bin_N)] in '1':
            cnt = 0

    return c

print(solution(1041))