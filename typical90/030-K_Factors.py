# https://atcoder.jp/contests/typical90/tasks/typical90_ad
# 普通にエラトステネスで素因数分解 O(NlogNlogN)

N, K = map(int, input().split())

def eratosthenes(n, k):
    prime = [0, 0] + [0] * (n-1)
    for p in range(2, n+1):
        if prime[p] != 0:
            continue
        for k in range(p, n+1, p):
            prime[k] += 1
    return prime

ss = eratosthenes(N, K)
ans = 0
for s in ss:
    if s >= K:
        ans += 1

print(ans)


