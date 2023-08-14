import math

def ans(A, B):
    if A == B:
        return 0

    X = min(A, B) + 1
    return math.ceil((B - X) / 2) + math.ceil((X - A) / 2)


if __name__ == '__main__':
    T = int(input())
    for _ in range(0, T):
        [A, B] = list(map(int, input().rstrip().split()))
        print(ans(A, B))
