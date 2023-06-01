# https://atcoder.jp/contests/typical90/tasks/typical90_aq

H, W = map(int, input().split())
sr, sc = map(int, input().split())
tr, tc = map(int, input().split())
maze = []
for _ in range(H):
    m = list(input())
    maze.append(m)

from collections import deque

q = deque([(sr-1, sc-1, 0), (sr-1, sc-1, 1), (sr-1, sc-1, 2), (sr-1, sc-1, 3)])
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
min_cost = [[[float('Inf')] * 4 for _ in range(W)] for _ in range(H)]
for i in range(4):
    min_cost[sr-1][sc-1][i] = 0

while q:
    now_r, now_c, pos = q.popleft()
    for nxt_pos in range(4):
        dr, dc = dxy[nxt_pos]
        nr, nc = now_r+dr, now_c+dc
        if nr < 0 or H <= nr or nc < 0 or W <= nc: # エリア外
            #print("outside")
            continue
        if maze[nr][nc] == '#': # 壁
            #print("wall")
            continue
        if pos == nxt_pos:  # 同じ方向への移動
            #print("add q same pos")
            n_cost = min_cost[now_r][now_c][pos]
        else:
            #print("add q different pos")
            n_cost = min_cost[now_r][now_c][pos] + 1
        if min_cost[nr][nc][nxt_pos] <= n_cost:
            continue
        min_cost[nr][nc][nxt_pos] = n_cost
        if pos == nxt_pos:
            q.appendleft((nr, nc, nxt_pos))
        else:
            q.append((nr, nc, nxt_pos))

print(min(min_cost[tr-1][tc-1]))








