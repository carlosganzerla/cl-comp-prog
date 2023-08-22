def ans(C, A):
    delay = A[0]
    front = A[0]
    back = 0
    for i in range(1, len(A)):
        front += A[i]
        back += A[i - 1]
        if front > back + delay:
            delay = front - back

    return (C - 1) * delay


if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        N = int(input().rstrip())
        A = list(map(int, input().rstrip().split()))
        C, *_ = tuple(map(int, input().rstrip().split()))
        print(ans(C, A))
