MOD = 10**9 + 7

def ans(A, N):
    A.sort()
    maxes = 0
    mins = 0
    for i in range(0, N):
        mins += (A[i] * 2**(N - i)) % MOD
        maxes += (A[N - i - 1] * 2**(N - i)) % MOD


    return (maxes - mins) % MOD

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        N = int(input().rstrip())
        A = list(map(int, input().rstrip().split()))
        print(ans(A, N))
