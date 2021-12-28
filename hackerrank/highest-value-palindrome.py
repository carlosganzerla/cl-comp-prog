#!/bin/python3

def highest_value_palindrome(s, n, k):
    if len(s) == 1 and k:
        return '9'

    l = list(s[0:n//2])
    m = list(s[n//2:n-n//2])
    r = list(s[n-n//2:][::-1])
    d = [ i for i in range(0, len(l)) if l[i] != r[i] ]
    k_min = len(d)

    if k_min > k:
        return '-1'

    u = k

    for i in range(0, len(l)):
        cost = int(l[i] != '9') + int(r[i] != '9')
        kmin_dec = int(i in d)
        if cost + k_min - kmin_dec > u:
            break
        u -= cost
        l[i] = '9'
        r[i] = '9'
        if kmin_dec:
            k_min -= kmin_dec
            d.remove(i)

    for i in d:
        l[i] = max(l[i], r[i])
        r[i] = max(l[i], r[i])
        u -= 1

    if u and m:
        m[0] = '9'


    return ''.join(l + m + r[::-1])
    # Write your code here

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highest_value_palindrome(s, n, k)

    print(result)

