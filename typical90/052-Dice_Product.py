N = int(input())
A = []
ans = 1
NUM = 1000000007
for _ in range(N):
    a = list(map(int, input().split()))
    sum_a = sum(a)
    ans *= sum_a
    ans %= NUM

print(ans)

