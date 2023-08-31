def ans(A, N):
    first_max = 0
    last_max = 0
    max_e = 0
    for i in range(0, N):
        if A[i] > max_e:
            first_max = i
            last_max = i
            max_e = A[i]
        elif A[i] == max_e:
            last_max = max(last_max, i)


    return max(N - N // 2 - last_max + first_max, 0)


if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        N = int(input().rstrip())
        A = list(map(int, input().rstrip().split()))
        print(ans(A, N))
