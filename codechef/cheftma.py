def ans(N, A, B, C, D):
    diff = [A[i] - B[i] for i in range(0, N)]
    buttons = C + D
    buttons.sort(reverse=True)
    diff.sort(reverse=True)
    M = len(buttons)
    i = 0
    for j in range(0, M):
        if i >= N:
            break
        elif diff[i] >= buttons[j]:
            diff[i] = diff[i] - buttons[j]
            i += 1


    return sum(diff)

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        N, *_ = tuple(map(int, input().rstrip().split()))
        A = list(map(int, input().rstrip().split()))
        B = list(map(int, input().rstrip().split()))
        C = list(map(int, input().rstrip().split()))
        D = list(map(int, input().rstrip().split()))
        print(ans(N, A, B, C, D))
