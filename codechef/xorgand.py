import math

def get_msb_idx(n):
    if n == 0:
        return 0

    return int(math.log2(n)) + 1

if __name__ == '__main__':
    T = int(input().rstrip())
    for _ in range(0, T):
        N = int(input().rstrip())
        A = list(map(int, input().rstrip().split()))
        msbs = [[0 for _ in range(0,32)]]
        for i in range(1, N + 1):
            seed = list(msbs[i - 1])
            seed[get_msb_idx(A[i - 1])] += 1
            msbs.append(seed)

        Q = int(input().rstrip())
        for _ in range(0, Q):
            [L, R, X] = list(map(int, input().rstrip().split()))
            idx = get_msb_idx(X)
            ans = R - L + 1 - msbs[R][idx] + msbs[L - 1][idx]
            print(ans)
