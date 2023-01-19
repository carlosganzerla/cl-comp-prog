

if __name__ == '__main__':
    for _ in range(0, int(input())):
        inp = input().split(" ")
        n = int(inp[0])
        k = int(inp[1])
        array = map(int, input().split(" "))
        if n == 1:
            print("YES")
        else:
            minval = 2**32
            maxval = -1
            for a in array:
                minval = min(minval, a)
                maxval = max(maxval, a)

            if maxval + minval <= k:
                print("YES")
            else:
                print("NO")
