# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam to I/O for Women 2022 - Problem D. Inventor Outlasting
# https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870/0000000000a33fb0
#
# Time:  O(R^3 * C^3)
# Space: O(R^2 * C^2)
#

from functools import lru_cache
from collections import Counter

def round_up(x, parity):
    return x+((x%2)^parity)

def round_down(x, parity):
    return x-((x%2)^parity)

def mex(lookup):
    result = 0
    while result in lookup:
        result += 1
    return result

def inventor_outlasting():
    @lru_cache(None)
    def memoization(l, r, u, d):
        lookup = set()
        for x in range(l, r+1, 2):
            # 0 <= i < len(L) and  0 <= j < len(L[0]) and u <= y <= d
            # => 0 <= y+x <= 2*len(L)-1 and  0 <= y-x <= 2*len(L[0])-1 and u <= y <= d
            # => max(-x, x, u) <= y <= min(2*len(L)-x-1, 2*len(L[0])+x-1, d)
            for y in range(max(-x, x, u), min(2*len(L)-x-1, 2*len(L[0])+x-1, d)+1, 2):
                if L[(y+x)//2][(y-x)//2] != 'X':
                    continue
                lookup.add(memoization(l, x-2, u, y-2)^
                           memoization(l, x-2, y+2, d)^
                           memoization(x+2, r, u, y-2)^
                           memoization(x+2, r, y+2, d))
        return mex(lookup)

    R, C = map(int, input().strip().split())
    L = [input().strip() for _ in range(R)]
    cnt = [Counter(), Counter()]
    for parity in range(2):
        l, r = round_up(0-(C-1), parity), round_down((R-1)-0, parity)
        u, d = round_up(0+0, parity), round_down((R-1)+(C-1), parity)
        for i in range(R):
            for j in range((i%2)^parity, C, 2):
                if L[i][j] != 'X':
                    continue
                x, y = i-j, i+j
                g = (memoization(l, x-2, u, y-2)^
                     memoization(l, x-2, y+2, d)^
                     memoization(x+2, r, u, y-2)^
                     memoization(x+2, r, y+2, d))
                cnt[parity][g] += 1
    grundy = list(map(mex, cnt))
    return cnt[0][grundy[1]]+cnt[1][grundy[0]]

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, inventor_outlasting()))
