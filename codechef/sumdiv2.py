MAX = 10 ** 18

def ans(x, y):
    c = x * y
    m = 1 if c > MAX / 10 else 10
    return c * m  - x - y



if __name__ == '__main__':
    t = int(input());
    for _ in range(0, t):
        x, y = tuple(map(int, input().rstrip().split()))
        print(ans(x, y))
