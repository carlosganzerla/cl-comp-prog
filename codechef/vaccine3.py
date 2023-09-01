from math import ceil

def ans(G, P, X):
    all_groups = sum(X[G - 1:])
    max_wait = int(ceil(all_groups / P))
    min_wait = (all_groups - X[G - 1]) // P + 1
    return (min_wait, max_wait)


if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        G, P, *X = tuple(map(int, input().rstrip().split()))
        print(*ans(G, P, list(X)))
