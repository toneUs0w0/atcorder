# https://atcoder.jp/contests/typical90/tasks/typical90_l
# lv 4

# おそらくUnion-Find木
# 色を塗ったマスに既に隣接する赤マスがあるなら、パスをunion-findに追加する

from collections import defaultdict

H, W = map(int, input().split())
Q = int(input())
Qry = []
for _ in range(Q):
    q = list(map(int, input().split(" ")))
    Qry.append(q)

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
    
red_or_not = [[False] * W for _ in range(H)]

uf = UnionFind(H*W+1)

for q in Qry:
    if q[0] == 1:
        r, c = q[1], q[2]
        n = (r-1) * W + c
        red_or_not[r-1][c-1] = True
        for dh, dw in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
            if 1 <= r + dh <= H and 1 <= c + dw <= W:
                if red_or_not[r + dh - 1][c + dw - 1]:
                    m = (r + dh - 1) * W + c + dw
                    uf.union(n, m)
                    #print("union: {} - {}".format(n, m))
    else:
        ra, ca, rb, cb = q[1], q[2], q[3], q[4]
        #print("same judge {} - {}".format((ra-1)*W + ca, (rb-1)*W + cb))
        if red_or_not[ra-1][ca-1] and red_or_not[rb-1][cb-1] and uf.same((ra-1)*W + ca, (rb-1)*W + cb):
            print("Yes")
        else:
            print("No")
                