from math import ceil

def ans(A, date_birth, date_current):
    yb, mb, db = date_birth
    yc, mc, dc = date_current
    full_leaps = max(0, int(ceil(yc / 4)) - int(ceil(yb / 4)))
    return (
        (yc - yb) * sum(A) + full_leaps + dc + sum(A[0:mc - 1]) - db - sum(A[0:mb - 1]) + 1
    )

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        _ = int(input().rstrip())
        A = list(map(int, input().rstrip().split()))
        date_birth = tuple(map(int, input().rstrip().split()))
        date_current = tuple(map(int, input().rstrip().split()))
        print(ans(A, date_birth, date_current))
