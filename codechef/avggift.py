def ans(X, S):
    satisfies = X <= max(S) and X >= min(S)
    return 'YES' if satisfies else 'NO'


if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        [N, X] = list(map(int, input().rstrip().split(' ')))
        S = list(map(int, input().rstrip().split()))
        print(ans(X, S))

