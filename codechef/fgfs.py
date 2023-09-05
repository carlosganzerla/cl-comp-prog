class Tree:
    def __init__(self, s, f) -> None:
        self.left = None
        self.right = None
        self.f = f
        self.s = s
        self.available = 1

    def _add(self, s, f, acc):
        if s < self.f and self.s < self.f:
            if self.left:
                return self.left._add(s, f, acc)
            else:
                self.left = Tree(s, f)
                return acc
        else:
            if self.right:
                return self.right._add(s, f, acc + 1)
            else:
                self.right = Tree(s, f)
                return acc + 1

    def add(self, s, f):
        self.available = max(self.available, self._add(s, f, 1))

def ans(N, K, C):
    trees = {}
    for s, f, k in C:
        if k not in trees:
            trees[k] = Tree(s, f)
        else:
            trees[k].add(s, f)

    return sum([t.available for t in trees.values()])


if __name__ == "__main__":
    T = int(input().rstrip())
    for i in range(0, T):
        N, K = tuple(map(int, input().rstrip().split()))
        C = []
        for _ in range(0, N):
            C.append(tuple(map(int, input().rstrip().split())))
        print(ans(N, K, C))
