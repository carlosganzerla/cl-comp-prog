def ans(S, N):
    chars = {}
    gap = N
    for i in reversed(range(0, N)):
        if S[i] in chars:
            gap = min(gap, chars[S[i]] - i)

        chars[S[i]] = i

    return N - gap


if __name__ == "__main__":
    T = int(input().rstrip())
    for i in range(0, T):
        N = int(input().rstrip())
        S = input().rstrip()
        print(ans(S, N))
