# lv 5

# 普通にやるとレンガN個についてMマスの高さ調査, 高さの更新より O(NM)
# lからrまでの最大の高さを取得 & lからrの最大値を更新の高速化

W, N = map(int, input().split())
blocks = []
s = set()
for _ in range(N):
    l, r = map(int, input().split())
    blocks.append((l, r))
    s.add(l)
    s.add(r)

# 次元圧縮
id_l = list(s)
id_l.sort()
w2id = [-1] * (W + 1)
num = 0
for i in id_l:
    w2id[i] = num
    num += 1
new_blocks = []
for l, r in blocks:
    new_blocks.append((w2id[l], w2id[r]))

# 遅延セグメント木の実装

def segfunc(x,y):
    return max(x,y)

class LazySegTree_RUQ:
    def __init__(self,init_val,segfunc,ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1<<(n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        self.lazy = [None]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.segfunc(self.tree[2*i],self.tree[2*i+1])

    def gindex(self,l,r):
        l += self.num
        r += self.num
        lm = l>>(l&-l).bit_length()
        rm = r>>(r&-r).bit_length()
        while r>l:
            if l<=lm:
                yield l
            if r<=rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1

    def propagates(self,*ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[i] = None
            self.lazy[2*i] = v
            self.lazy[2*i+1] = v
            self.tree[2*i] = v
            self.tree[2*i+1] = v

    def update(self,l,r,x):
        ids = self.gindex(l,r)
        self.propagates(*self.gindex(l,r))
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                self.lazy[l] = x
                self.tree[l] = x
                l += 1
            if r&1:
                self.lazy[r-1] = x
                self.tree[r-1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])

    def query(self,l,r):
        ids = self.gindex(l,r)
        self.propagates(*self.gindex(l,r))
        res = self.ide_ele
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                res = self.segfunc(res,self.tree[l])
                l += 1
            if r&1:
                res = self.segfunc(res,self.tree[r-1])
            l >>= 1
            r >>= 1
        return res
    
_tmp = [0] * len(s)
seq = LazySegTree_RUQ(_tmp, segfunc, 0)

for l, r in new_blocks:
    ans = seq.query(l, r+1) + 1
    print(ans)
    seq.update(l, r+1, ans)




    
        



