# cook your dish here
def ans(n, k, s):
    return (s - n * n) // (k - 1)


if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        print(ans(*map(int, input().split())))
