from math import log10
MAX = 10**9
MOD = MAX + 7

def ans(L, R):
    ans = 0
    for i in range(int(log10(L)), int(log10(R)) + 1):
        first = max(L, 10**i)
        last = min(R, 10**(i + 1) - 1)
        term = (i + 1) * (last - first + 1) * (first + last) / 2
        ans = (ans + term) % MOD

    return ans

if __name__ == '__main__':
    t = int(input().rstrip())
    for i in range(0, t):
        L, R = tuple(map(int, input().rstrip().split()))
        b = list(map(int, input().rstrip().split()))
        print(ans(L, R))
