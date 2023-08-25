MOVIES = set("ABCD")
TIMES = {"12", "3", "6", "9"}


def ans(requests):
    req_map = {m + t: 0 for m in MOVIES for t in  TIMES }
    for m, t in requests:
        req_map[m + t] += 1

    exclude = set()
    req_map = {k: v for k, v in req_map.items() if v }
    sorted_reqs = sorted(req_map.items(), reverse=True, key=lambda kv: kv[1])
    price = 100
    ans = 0
    for mt, v in sorted_reqs:
        m, t = mt[0], mt[1:]
        if t not in exclude and m not in exclude:
            ans += v * price
            price -= 25
            exclude.add(m)
            exclude.add(t)


    for m in MOVIES:
        if m not in exclude:
            ans -= 100

    return ans

if __name__ == '__main__':
    T = int(input().rstrip())
    total = 0
    for i in range(0, T):
        N = int(input().rstrip())
        requests = []
        for _ in range(0, N):
            requests.append(tuple(input().rstrip().split()))
        r = ans(requests)
        total += r
        print(r)

    print(total)
