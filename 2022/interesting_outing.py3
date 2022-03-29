# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam to I/O for Women 2022 - Problem C. Interesting Outing
# https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870/0000000000a33bc7
#
# Time:  O(N)
# Space: O(N)
#

def bfs(adj, u):
    q = [u]
    dist = [-1]*len(adj)
    dist[u] = 0
    while q:
        new_q = []
        for u in q:
            for v, d in adj[u]:
                if dist[v] != -1:
                    continue
                dist[v] = dist[u]+d
                new_q.append(v)
        q = new_q
    return dist

def interesting_outing():
    N = int(input())
    adj = [[] for _ in range(N)]
    total = 0
    for _ in range(N-1):
        A, B, C = map(int, input().strip().split())
        adj[A-1].append((B-1, C))
        adj[B-1].append((A-1, C))
        total += C
    dist = bfs(adj, 0)
    start = max(range(N), key=dist.__getitem__)
    max_dist = max(bfs(adj, start))
    return 2*total-max_dist

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, interesting_outing()))
