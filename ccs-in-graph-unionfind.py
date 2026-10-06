class UnionFind:
    def __init__(self, members):
        self.parents = [i for i in range(len(members))]
        self.rank = [0 for i in range(len(members))]

    def union(self, m1, m2) -> bool:
        p1 = self.find(m1)
        p2 = self.find(m2)

        if p1 == p2:
            return False

        if self.rank[p1] == self.rank[p2]:
            self.parents[p1] = p2
            self.rank[p2] += 1
            return True
        elif self.rank[p1] > self.rank[p2]:
            self.parents[p2] = p1
            return True
        else:
            self.parents[p1] = p2
            return True
    
    def find(self, m):
        while self.parents[m] != m:
            return self.find(self.parents[m])

        return m
    

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:

        uf = UnionFind([i for i in range(n)])

        ccs = n

        for u, v in edges:
            if uf.union(u, v):
                ccs -= 1

        return ccs


'''
Practice implement union find. Straightforward
'''
