from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

N = int(input())
Q = int(input())
query = []
for _ in range(Q):
    query.append(tuple(map(int, input().split())))

uf = UnionFind(N+1)

query2 = []
pipe = [-1] * (N)
for t, x, y, v in query:
    if t == 0:
        uf.union(x, y)
        pipe[x] = v
    else:
        if uf.same(x, y) == False:
            query2.append((0, 0, 0, 0))    
        else:
            query2.append((1, x, y, v))

#print(pipe)
tmp = [None] * (N+1)
tmp[1] = 0
cnts = [None] * (N+1)
cnt = 0
for j in range(1, N):
    if pipe[j] == -1:
        cnt = 0
        tmp[j+1] = 0
    else:
        cnts[j] = cnt
        cnt += 1
        tmp[j+1] = pipe[j] - tmp[j]
#print(tmp)
#print(cnts)
for t, x, y, v in query2:
    if t == 0:
        print("Ambiguous")
    else:
        dv = tmp[x] - v
        if x%2 == y%2:
            print(tmp[y] - dv)
        else:
            print(tmp[y] + dv)





