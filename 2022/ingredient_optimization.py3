# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam to I/O for Women 2022 - Problem B. Ingredient Optimization
# https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870/0000000000a341ec
#
# Time:  O(N + DlogD)
# Space: O(D)
#

from heapq import heappush, heappop

def check(min_heap, cnt):
    while min_heap and cnt:
        c = min(min_heap[0][1], cnt)
        min_heap[0][1] -= c
        if not min_heap[0][1]:
            heappop(min_heap)
        cnt -= c
    return cnt == 0

def ingredient_optimization():
    D, N, U = map(int, input().strip().split())
    M_L_E = [list(map(int, input().strip().split())) for _ in range(D)]
    O = list(map(int, input().strip().split()))
    min_heap = []
    result = left = 0
    for x in O:
        while left < len(M_L_E) and M_L_E[left][0] <= x:
            heappush(min_heap, [M_L_E[left][0]+M_L_E[left][2], M_L_E[left][1]])
            left += 1
        while min_heap and min_heap[0][0] <= x:
            heappop(min_heap)
        if not check(min_heap, U):
            break
        result += 1
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, ingredient_optimization()))
