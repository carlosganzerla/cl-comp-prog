def ans(arr):
    n = len(arr)
    sums = {}
    for i in range(0, n):
        for j in range(i + 1, n):
            sum = arr[i] + arr[j]
            if (sum in sums and
                    i not in sums[sum] and
                    j not in sums[sum]):
                sums[sum][i] = True
                sums[sum][j] = True
            elif sum not in sums:
                sums[sum] = { i: True, j: True }
    return max([ len(v) for _, v in sums.items() ])

if __name__ == '__main__':
    input()
    arr = list(map(int, input().rstrip().split()))
    result = ans(list(set(arr)))
    print(result)
