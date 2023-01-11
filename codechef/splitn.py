# cook your dish here
from math import log2

def ops(n):
    d = log2(n)
    dtrunc = int(d)
    i = 0
    while d != dtrunc:
        n = n - 2**dtrunc
        d = log2(n)
        dtrunc = int(d)
        i += 1

    return i

if __name__ == '__main__':
    t = int(input());
    for _ in range(0, t):
        print(ops(int(input())))



