def ans(A, N):
    M = []
    result = ["0" for _ in range(0,32)]
    for a in A:
        M.append(list(bin(a)[2:].zfill(32)))


    for b in range(0, 32):
        count = 0
        for i in range(0, N):
            if M[i][b] == "1":
                count += 1
                if count > 1:
                    result[b] = "1"
                    break

    return int("".join(result), 2)

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        N = int(input().rstrip())
        A = list(map(int, input().rstrip().split()))
        print(ans(A, N))
