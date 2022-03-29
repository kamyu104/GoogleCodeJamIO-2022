# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam to I/O for Women 2022 - Problem A. Inversions Organize
# https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870/0000000000a33e95
#
# Time:  O(N^2)
# Space: O(1)
#

def inversions_organize():
    N = int(input())
    C = [input().strip() for _ in range(2*N)]
    cnt = [[0]*2 for _ in range(2)]
    for i in range(len(C)):
        for j, x in enumerate(C[i]):
            cnt[i//N][j//N] += int(x == 'I')
    return abs(cnt[0][0]-cnt[1][1])+abs(cnt[1][0]-cnt[0][1])

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, inversions_organize()))
