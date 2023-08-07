def ans(A_B, R):
    A_B = list(sorted(A_B, key=lambda a_b: a_b[0] - a_b[1]))
    result = 0
    for a, b in A_B:
        if R >= a:
            sweets = (R - a) // (a - b) + 1
            result += sweets
            R = R - (a - b) * sweets

    return result

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        [N, R] = list(map(int, input().rstrip().split()))
        A = list(map(int, input().rstrip().split()))
        B = list(map(int, input().rstrip().split()))
        print(ans(list(zip(A, B)), R))
