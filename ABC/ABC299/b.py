N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

max_ans = -1
ans = 0
if T in C:
    for i in range(N):
        c = C[i]
        r = R[i]
        if c == T:
            if r > max_ans:
                max_ans = r
                ans = i + 1

    print(ans)
else:
    T = C[0]
    max_ans = R[0]
    ans = 1
    for i in range(1, N):
        c = C[i]
        r = R[i]
        if c == T:
            if r > max_ans:
                max_ans = r
                ans = i + 1
    print(ans)