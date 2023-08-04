def ans(A):
    max_cont = 0
    second_max_cont = 0
    zero_count = 0
    for a in A:
        if a == 0:
            zero_count += 1
        else:
            if zero_count > max_cont:
                second_max_cont = max_cont
                max_cont = zero_count
            elif zero_count > second_max_cont:
                second_max_cont = zero_count
            zero_count = 0

    if max_cont % 2 == 1 and max_cont / 2 > second_max_cont:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    T = int(input().rstrip())
    for _ in range(0, T):
        input()
        A = list(map(int, input().rstrip().split()))
        ans(A)
