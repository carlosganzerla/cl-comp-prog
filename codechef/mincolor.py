def ans(N, M, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    collision = N + M
    C = [[0 for _ in range(0, M)] for _ in range(0, N)]
    for i in range(0, N):
        for j in range(0, M):
            if (i + j) % 2 == (x1 + y1) % 2:
                if (i, j) == (x2, y2):
                    C[i][j] = 2
                    C[i - 1][j] = 3
                    C[i][j - 1] = 3
                    collision = i + j
                else:
                    C[i][j] = 1
            else:
                C[i][j] = 2 if abs(collision - i - j) != 1 else 3


    for row in C:
        print(*row)



if __name__ == '__main__':
    T = int(input())
    for _ in range(0, T):
        N, M = tuple(map(int, input().rstrip().split()))
        x1, y1 = tuple(map(int, input().rstrip().split()))
        x2, y2 = tuple(map(int, input().rstrip().split()))
        p1 = (x1 - 1, y1 - 1)
        p2 = (x2 - 1, y2 - 1)
        ans(N, M, p1, p2)
