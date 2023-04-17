N = int(input())
A = []
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)
B = []
for _ in range(N):
    b = list(map(int, input().split()))
    B.append(b)

def check(a, b):
    f = True
    for n in range(N):
        for m in range(N):
            if a[n][m] == 1:
                if b[n][m] == 1:
                    continue
                else:
                    f = False
    return f

for _ in range(4):
    newA = [[0] * (N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            newA[N-1-j][i] = A[i][j]
    rtn = check(newA, B)
    if rtn:
        print("Yes")
        exit()
    A = newA

print("No")


