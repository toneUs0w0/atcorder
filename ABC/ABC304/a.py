N = int(input())
min_a = float('Inf')
st = 0
names = []
for n in range(N):
    s, a = map(str, input().split())
    ai = int(a)
    if ai < min_a:
        st = n
        min_a = ai
    names.append(s)

index = st
for i in range(N):
    index = (st + i) % N
    print(names[index])
    
