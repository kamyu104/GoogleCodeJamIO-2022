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
    return x+(parity^(x%2))

def round_down(x, parity):
    return x-(parity^(x%2))

def mex(lookup):
    result = 0
    while result in lookup:
        result += 1
    return result

def inventor_outlasting():
    depth = [0]
    cnt = [Counter(), Counter()]
    @lru_cache(None)
    def memoization(l, r, u, d):
        depth[0] += 1
        lookup = set()
        for x in range(l+2, r, 2):
            # 0 <= i < len(L) and  0 <= j < len(L[0]) and u+2 <= y < d
            # => 0 <= y+x < 2*len(L) and  0 <= y-x < 2*len(L[0]) and u+2 <= y < d
            # => max(-x, x, u+2) <= y < min(2*len(L)-x, 2*len(L[0])+x, d)
            for y in range(max(-x, x, u+2), min(2*len(L)-x, 2*len(L[0])+x, d), 2):
                if L[(y+x)//2][(y-x)//2] != 'X':
                    continue
                g = (memoization(l, x, u, y)^
                     memoization(l, x, y, d)^
                     memoization(x, r, u, y)^
                     memoization(x, r, y, d))
                lookup.add(g)
                if depth[0] == 1:
                    cnt[l%2][g] += 1
        depth[0] -= 1
        return mex(lookup)

    R, C = map(int, input().strip().split())
    L = [input().strip() for _ in range(R)]
    for parity in range(2):
        memoization(round_up(0-(C-1), parity)-2,
                    round_down((R-1)-0, parity)+2,
                    round_up(0+0, parity)-2,
                    round_down((R-1)+(C-1), parity)+2)
    grundy = list(map(mex, cnt))
    return cnt[0][0^grundy[1]]+cnt[1][0^grundy[0]]

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, inventor_outlasting()))
