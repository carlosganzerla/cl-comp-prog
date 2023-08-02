def ans(A, L, R, X):
    pass

def make_bin(n):
    return bin(int(n))[2:].zfill(32)

if __name__ == '__main__':
    T = int(input().rstrip())
    for _ in range(0, T):
        N = int(input().rstrip())
        A = [make_bin(a) for a in input().rstrip().split()]
        zeros = [0 for _ in range(0, 32)]
        for a in A:
            for i in range(0,32):
                if a[i] == '0':
                    zeros[i] += 1

        # Q = int(input().rstrip())
        # for _ in range(0, Q):
        #     [L, R, X] = list(map(int, input().rstrip().split()))
        #     print(ans(A, L, R, X))


# TODO
# Create a matrix of bits line is the array index, column is the bit position
# Create a column of cumulative 0 count, line is the array index, column is the number of zeros up to that index

# Check the mystic numbers count with respect to X in an interval L to R:
# Get the cumulative 0 count from L to R (i.e.) (Zero count R) - (Zero count (L - 1))
# MSB of X is 1 -> number of mystic stuff is the zero count of the MSB position
# MSB of X is 0 -> number of ones (interval LR length - zero count of MSB position)

