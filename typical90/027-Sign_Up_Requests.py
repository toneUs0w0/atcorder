# https://atcoder.jp/contests/typical90/tasks/typical90_aa
# lv 2

# setで管理

N = int(input())
S = []
for _ in range(N):
    n = input()
    S.append(n)

namelist = set()
n = 1
for s in S:
    if s not in namelist:
        namelist.add(s)
        print(n)
    n += 1
