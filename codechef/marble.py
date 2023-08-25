CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWELS = "aeiou"
LETTERS  = CONSONANTS + VOWELS

def get_cost(p: str, s: str):
    if p == s:
        return 0
    elif p in CONSONANTS and s in CONSONANTS or p in VOWELS and s in VOWELS:
        return 2
    else:
        return 1


def ans(N: int, P: str, S: str):
    costs = { letter: 0 for letter in LETTERS }
    ans = 0
    for i in range(0, N):
        p = P[i]
        s = S[i]
        if p != "?" and s != "?":
            ans += get_cost(p, s)
        elif p == "?" and s != "?":
            for letter in costs:
                costs[letter] += get_cost(letter, s)
        elif p != "?" and s == "?":
            for letter in costs:
                costs[letter] += get_cost(p, letter)

    ans += min(costs.values())
    return ans

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        N = int(input().rstrip())
        P = input()
        S = input()
        print(ans(N, P, S))
