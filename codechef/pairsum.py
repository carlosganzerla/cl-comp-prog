def ans(arr, n):
    sums = {}
    for i in range(0, n):
        for j in range(i + 1, n):
            sum = arr[i] + arr[j]
            if sum in sums:
                sums[sum] += 1
            else:
                sums[sum] = 1

    return 2 * max([ v for _, v in sums.items() ])

if __name__ == '__main__':
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    result = ans(arr, n)
    print(result)
