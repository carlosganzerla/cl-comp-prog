from math import ceil

def ans(N, K, C):
    m = 1
    t = 0
    for i in reversed(range(1, N)):
        t += (C[i] - C[i - 1] - 1) * ceil(m / K)
        m += 1

    t += (C[0] - 1) * ceil(m / K)
    return int(t)

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        N, K = list(map(int, input().rstrip().split()))
        C = list(map(int, input().rstrip().split()))
        print(ans(N, K, C))
