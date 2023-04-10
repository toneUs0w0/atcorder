# https://atcoder.jp/contests/typical90/tasks/typical90_r
# lv 3

# ゴリゴリに計算すれば良い

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
E = []
for _ in range(Q):
    e = int(input())
    E.append(e)

import math

def arg(e):
    #print("case: {}".format(e))
    cita = (2 * e * math.pi) / T
    #print("cita: {}".format(cita))
    p_x = 0
    p_y = (-1 * L * math.sin(cita)) / 2
    p_z = (1 - math.cos(cita)) * L / 2
    #print("player : [{}, {}, {}]".format(p_x, p_y, p_z))

    dist_xy = math.sqrt(math.pow(X, 2) + math.pow(Y - p_y, 2))
    dist_z = p_z
    ans = math.degrees(math.atan(dist_z / dist_xy))
    print(ans)

for e in E:
    arg(e)