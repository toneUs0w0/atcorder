# https://atcoder.jp/contests/typical90/tasks/typical90_v
# lv 2

# A, B, Cの最大公約数を辺とするキューブになる
A, B, C = map(int, input().split())

import math
l = math.gcd(math.gcd(A, B), C)
print(A//l + B//l + C//l - 3)
