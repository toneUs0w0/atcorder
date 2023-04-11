# https://atcoder.jp/contests/typical90/tasks/typical90_t
# lv 3

# シンプルなlog演算
import math

a, b, c = map(int, input().split())

if a < c ** b:
    print("Yes")
else:
    print("No")
