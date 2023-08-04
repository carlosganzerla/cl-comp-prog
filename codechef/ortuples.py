def to_bit_array(n):
    return list(map(int, bin(n)[2:].zfill(32)))

def ans(P, Q, R):
    A_B = to_bit_array(P)
    B_C = to_bit_array(Q)
    C_A = to_bit_array(R)
    free = 0
    for i in range(0,32):
        s = A_B[i] + B_C[i] + C_A[i]
        if s == 1:
            return 0
        if s == 3:
            free += 1

    return 4 ** free


if __name__ == '__main__':
    for i in range(0, int(input())):
        [P, Q, R] = list(map(int, input().rstrip().split()))
        print(ans(P, Q, R))
