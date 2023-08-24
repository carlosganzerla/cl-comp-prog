def ans(N, S, T):
    none = 0
    programming = 0
    english = 0
    both = 0
    for i in range(0, N):
        skills = S[i] + T[i]
        if skills == "11":
            both += 1
        elif skills == "10":
            programming += 1
        elif skills == "01":
            english += 1
        else:
            none += 1

    result = 0
    # Full skill with no skill
    full_none = min(both, none)
    result += full_none
    both -= full_none
    # Semi-skilled together
    semi = min(english, programming)
    result += semi
    programming -= semi
    english -= semi

    # Combine full skilled with semi-skilled and full with full
    full_semi = min(both, max(programming, english))
    both -= full_semi
    result += full_semi + both // 2
    return result

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        N = int(input().rstrip())
        S = input().rstrip()
        T = input().rstrip()
        print(ans(N, S, T))
