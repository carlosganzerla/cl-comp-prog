def ans(S, N, K):
    diffs = []
    for i in range(0, N - 1):
        diffs.append(int(S[i] != S[i + 1]))

    print(diffs)

    current = sum(diffs[0:K])
    result = current
    for i in range(0, N - K - 1):
        current = current - diffs[i] + diffs[i + K]
        result += current

    return result


if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        [N, K] = list(map(int, input().rstrip().split()))
        print(ans(input(), N, K))
