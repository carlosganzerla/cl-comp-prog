def get_lcs(s: str, t: str, i: int, j: int) -> str:
    if i < 0 or j < 0:
        return ""
    elif s[i] == t[j]:
        return get_lcs(s, t, i - 1, j - 1) + s[i]
    else:
        return max(get_lcs(s, t, i - 1, j), get_lcs(s, t, i, j - 1), key=len)


def ans(strings):
    counts = []
    for s in strings:
        d = dict(a=0, b=0)
        counts.append(d)
        for c in s:
            d[c] += 1


    return min([min(*d.values()) for d in counts])

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        N = int(input().rstrip())
        strings = list([input().rstrip() for _ in range(0, N)])
        print(ans(strings))
