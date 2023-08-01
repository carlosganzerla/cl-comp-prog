def ans(A, B, N):
    deltas = {}
    for i in range(0, N - 1):
        left = B[i] - A[i]
        right = B[i] - A[i + 1]
        deltas[left] = deltas[left] + 1 if left in deltas else 1
        deltas[right] = deltas[right] + 1 if right in deltas else 1

    x_deltas = filter(lambda x: deltas[x] == N - 1, deltas)
    return min(x_deltas)


if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        N = int(input().rstrip())
        A = list(map(int, input().rstrip().split()))
        B = list(map(int, input().rstrip().split()))
        A.sort()
        B.sort()
        print(ans(A, B, N))
