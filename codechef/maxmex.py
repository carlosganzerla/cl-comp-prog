def ans(A, N, M):
    A.sort()
    last = 0
    result = N
    for i in range(0, N):
        if last < M - 1 and A[i] - last > 1:
            return -1
        elif A[i] == M:
            result -= 1

        last = A[i]


    return result

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        _, M = tuple(map(int, input().rstrip().split()))
        A = list(map(int, input().rstrip().split()))
        print(ans(A, len(A), M))
