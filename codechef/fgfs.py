def ans(N, K, C):
    compartments = {}
    ans = 0
    for s, f, k in C:
        if k not in compartments:
            compartments[k] = [(f, s)]
        else:
            compartments[k].append((f, s))

    for c in compartments.values():
        c.sort()
        max_val = 0
        for f, s in c:
            if s >= max_val:
                ans += 1
                max_val = f


    return ans


if __name__ == "__main__":
    T = int(input().rstrip())
    for i in range(0, T):
        N, K = tuple(map(int, input().rstrip().split()))
        C = []
        for _ in range(0, N):
            C.append(tuple(map(int, input().rstrip().split())))
        print(ans(N, K, C))
