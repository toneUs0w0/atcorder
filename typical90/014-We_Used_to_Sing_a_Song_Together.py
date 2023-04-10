# https://atcoder.jp/contests/typical90/tasks/typical90_n
# lv 3

# 家の位置と学校の位置をそれぞれ昇順にし、その順で対応付ければ良い
# 各家ごとにはより近い学校があるが、それを優先すると遠くなる家が必ず存在し、総和はそちらの方が大きい

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = 0
for n in range(N):
    ans += abs(A[n] - B[n])
print(ans)