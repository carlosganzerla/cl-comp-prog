#!/bin/python3

def is_fibo(n):
    f0 = 0
    f1 = 1
    while f1 < n:
        temp = f0
        f0 = f1
        f1 += temp

    return f1 == n

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = is_fibo(n)
        print('IsFibo' if result else 'IsNotFibo')


