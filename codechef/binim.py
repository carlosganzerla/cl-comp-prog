def ans(stacks, starter):
    max_dum = 0
    max_dee = 0
    for s in stacks:
        count = 0
        for e in s:
            if e == s[0]:
                count += 1
            else:
                break

        if s[0] == "0":
            max_dee = max(max_dee, count)
        else:
            max_dum = max(max_dum, count)

    if starter == "Dum":
        max_dee += 0.5
    else:
        max_dum += 0.5

    return "Dum" if max_dum > max_dee else "Dee"


if __name__ == "__main__":
    T = int(input().rstrip())
    for i in range(0, T):
        N, starter = tuple(input().rstrip().split())
        N = int(N)
        stacks = [input().rstrip() for _ in range(0, N)]
        print(ans(stacks, starter))
