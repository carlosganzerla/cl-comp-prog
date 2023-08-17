import math

def smallest_factor_before_sqrt(n):
    for i in reversed(range(2, int(math.sqrt(n)) + 1)):
        if n % i == 0:
            return i

    return 1

def ans(X, Y):
    n = smallest_factor_before_sqrt(Y)
    R1 = X // 2 + X % 2
    L1 = X // 2
    R2 = Y // n
    L2 = n
    if R1 < L2 or R2 < L1:
        print(L1, R1)
        print(L2, R2)
    else:
        print(-1)


if __name__ == "__main__":
    T = int(input())
    for _ in range(0, T):
        ans(*map(int, input().rstrip().split()))
