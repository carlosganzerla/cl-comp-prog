from itertools import permutations

MOVIES = [0, 1, 2, 3]
PRICES = [25, 50, 75, 100]


def ans(requests):
    slots = [[0 for _ in range(0, 4)] for _ in range(0, 4)]
    for m, t in requests:
        slots[int(t) // 3 - 1][ord(m) - ord("A")] += 1

    ans = -400
    for prices in permutations(PRICES):
        for movies in permutations(MOVIES):
            temp = 0
            for i in range(0, 4):
                if slots[i][movies[i]] == 0:
                    temp -= 100
                else:
                    temp += slots[i][movies[i]] * prices[i]

            ans = max(ans, temp)

    return ans


if __name__ == "__main__":
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
