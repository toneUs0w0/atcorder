# https://atcoder.jp/contests/typical90/tasks/typical90_ag
# 縦横２つ置きに置くのが最大個数

import math

H, W = map(int, input().split())
if H == 1 or W == 1:
    print(H * W)
else:
    print(math.ceil(H/2) * math.ceil(W/2))