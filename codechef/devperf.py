def ans(M, m, n):
    right_off = 0
    left_off = 0
    top_off = 0
    bot_off = 0

    for j in range(0, n):
        if all([M[i][j] == "." for i in range(0, m)]):
            left_off += 1
        else:
            break

    if left_off == n:
        return 0

    for j in range(0, n):
        if all([M[i][n - j - 1] == "." for i in range(0, m)]):
            right_off += 1
        else:
            break


    for i in range(0, m):
        if all([M[i][j] == "." for j in range(0, n)]):
            top_off += 1
        else:
            break

    for i in range(0, m):
        if all([M[m - i - 1][j] == "." for j in range(0, n)]):
            bot_off += 1
        else:
            break

    adjusted_n = n - left_off - right_off
    adjusted_m = m - top_off - bot_off

    return max(adjusted_n, adjusted_m) // 2 + 1

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        [m, n] = list(map(int, input().rstrip().split(' ')))
        M = [input() for _ in range(0, m)]
        print(ans(M, m, n))
