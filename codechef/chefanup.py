def ans(N, K, L):
    digits = [i for i in range(0, K)]
    remainder_stack = []
    L = L - 1

    while L > 0:
        remainder = L % K
        remainder_stack.append(remainder)
        L = L // K

    ans = []
    while remainder_stack:
        ans.append(digits[remainder_stack.pop()] + 1)

    ans = [1 for _ in range(0, N - len(ans))] + ans
    return ans

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        N, K, L = tuple(map(int, input().rstrip().split()))
        print(*ans(N, K, L))
