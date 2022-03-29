# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam to I/O for Women 2022 - Problem D. Inventor Outlasting
# https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870/0000000000a33fb0
#
# Time:  O(R^3 * C^3)
# Space: O(R^2 * C^2)
#

from collections import Counter
from functools import lru_cache

def mex(lookup):
    result = 0
    while result in lookup:
        result += 1
    return result

def norm(x, parity):
    return x+int(x%2 != parity)

def inventor_outlasting():
    @lru_cache(None)
    def memoization(parity, l, r, u, d):
        lookup = set()
        for x in range(norm(l+1, parity), r, 2):
            # 0 <= i < len(L) and  0 <= j < len(L[0]) and u+1 <= y < d
            # => 0 <= y+x < 2*len(L) and  0 <= y-x < 2*len(L[0]) and u+1 <= y < d
            # => max(-x, x, u+1) <= y < min(2*len(L)-x, 2*len(L[0])+x, d)
            for y in range(norm(max(-x, x, u+1), parity),  min(2*len(L)-x, 2*len(L[0])+x, d), 2):
                if L[(y+x)//2][(y-x)//2] != 'X':
                    continue
                lookup.add(memoization(parity, l, x, u, y)^
                           memoization(parity, l, x, y, d)^
                           memoization(parity, x, r, u, y)^
                           memoization(parity, x, r, y, d))
        return mex(lookup)

    R, C = map(int, input().strip().split())
    L = [input().strip() for _ in range(R)]
    l, r, u, d = 0-(C-1)-1, (R-1)-0+1, 0+0-1, (R-1)+(C-1)+1
    cnt = [Counter(), Counter()]
    for i in range(R):
        for j in range(C):
            if L[i][j] != 'X':
                continue
            x, y, parity = i-j, i+j, (i+j)%2
            g = (memoization(parity, l, x, u, y)^
                 memoization(parity, l, x, y, d)^
                 memoization(parity, x, r, u, y)^
                 memoization(parity, x, r, y, d))
            cnt[parity][g] += 1
    grundy = list(map(mex, cnt))
    return cnt[0][grundy[1]]+cnt[1][grundy[0]]

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, inventor_outlasting()))
