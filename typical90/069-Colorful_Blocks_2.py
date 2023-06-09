N, K = map(int, input().split())
NUM = 10**9 + 7
# 1
ans = K
if N == 1:
    print(ans)
    exit()

# 2
ans *= (K-1)
ans %= NUM
if N == 2:
    print(ans)
    exit()

if K <= 2:
    print(0)
    exit()

# 繰り返し２乗法
# (K-2)**(N-2)を計算

K2modNUM = []
K2modNUM.append(1 % NUM)
K2modNUM.append((K-2) % NUM)
for n in range(2, 1000000):
    K2modNUM.append(K2modNUM[n-1] * K2modNUM[n-1] % NUM)

n = N-2
i = 1
while n > 0:
    #print(n)
    if n % 2 == 1:
        ans *= K2modNUM[i]
        ans %= NUM
    i += 1
    n //= 2

print(ans)









