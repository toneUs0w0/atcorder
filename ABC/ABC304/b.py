N = int(input())

if N <= 1000 - 1:
    print(N)
elif N <= 10000 - 1:
    print(N - N%10)
elif N <= 100000 - 1:
    print(N - N%100)
elif N <= 1000000 - 1:
    print(N - N%1000)
elif N <= 10000000 - 1:
    print(N - N%10000)
elif N <= 100000000 - 1:
    print(N - N%100000)
elif N <= 1000000000 - 1:
    print(N - N%1000000)    