A = list(map(int, input().split()))

num = 1
ans = 0
for a in A:
    ans += a*num
    num *= 2
print(ans)

