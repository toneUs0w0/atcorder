# https://atcoder.jp/contests/typical90/tasks/typical90_al
# 最大公約数から最小公倍数を計算

import math

A, B = map(int, input().split())

g = math.gcd(A, B)
ans = (A * B) // g
if ans > 10**18:
    print("Large")
else:
    print(ans)
