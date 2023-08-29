def get_idx(e):
    if e > 7:
        return 4
    elif e == 7:
        return 3
    elif e > 4:
        return 2
    elif e == 4:
        return 1
    else:
        return 0

PRIO_MAP = [
    (3, [2, 0, 1, 3], "7"),
    (1, [0, 1, 3], "4"),
]

def ans(A, B):
    count_A = [0 for _ in range(0, 5)]
    count_B = [0 for _ in range(0, 5)]
    result = []
    for a in A:
        count_A[get_idx(int(a))] += 1

    for b in B:
        count_B[get_idx(int(b))] += 1

    for send_idx, recv_idxs, char in PRIO_MAP:
        for send, recv in [(count_A, count_B), (count_B, count_A)]:
            for i in recv_idxs:
                amount = min(send[send_idx], recv[i])
                send[send_idx] -= amount
                recv[i] -= amount
                for _ in range(0, amount):
                    result.append(char)

    result.sort(reverse=True)
    return "".join(result)


if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        A = input().rstrip()
        B = input().rstrip()
        print(ans(A, B))
