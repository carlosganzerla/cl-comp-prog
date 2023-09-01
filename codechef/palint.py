def ans(A, N, X):
    numbers = {}
    for a in A:
        freq, ops = numbers.get(a, (0, 0))
        numbers[a] = freq + 1, ops
        if a ^ X != a:
            freq, ops = numbers.get(a ^ X, (0, 0))
            numbers[a ^ X] = freq + 1, ops + 1

    max_freq = 0
    maxes_ops = []
    for freq, ops in numbers.values():
        if freq > max_freq:
            max_freq = freq
            maxes_ops = [ops]
        elif freq == max_freq:
            maxes_ops.append(ops)

    return max_freq, min(maxes_ops)

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        N, X = tuple(map(int, input().rstrip().split()))
        A = list(map(int, input().rstrip().split()))
        print(*ans(A, N, X))
