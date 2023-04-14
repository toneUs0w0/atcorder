# https://atcoder.jp/contests/typical90/tasks/typical90_x
# lv 2

# AとBの各要素の絶対値の合計分の変更が必要

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

_abs = 0
for n in range(N):
    _abs += abs(A[n] - B[n])

if _abs > K:
    print("No")
elif (K - _abs) % 2 == 0:
    print("Yes")
else:
    print("No") 
