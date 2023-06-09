N, K = map(int, input().split())
n = N
for _ in range(K):
    num = 0
    p = 10
    q = 1
    for i in range(100):
        num += (n % p) * q
        n //= 10
        q *= 8
        if n <= 0:
            break
    #print(num)
    num2 = 0
    q = 1
    for i in range(100):
        num2 += (num%9) * q
        q *= 10
        num //= 9
        if num <= 0:
            break
    #print(num2)
    s_num2 = list(str(num2))
    for idx in range(len(s_num2)):
        if s_num2[idx] == '8':
            s_num2[idx] = '5'
    n = int(''.join(s_num2))
print(n)
    

    
