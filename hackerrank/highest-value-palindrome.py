#!/bin/python3

def highest_value_palindrome(s, n, k):
    if len(s) == 1 and k:
        return '9'
    l = list(s[0:n//2])
    m = list(s[n//2:n-n//2])
    r = list(s[n-n//2:][::-1])
    assert len(l) == len(r)
    assert len(m) <= 1
    d = [ i for i in range(0, len(l)) if l[i] != r[i] ]
    u = k
    for i in reversed(d):
        if u > 0 and l[i] != r[i]:
            l[i] = max(l[i], r[i])
            r[i] = l[i]
            u -= 1
        else:
            return '-1'

    for i in range(0,len(l)):
        debit = 0 if i in d else 1
        if u > 0:
            if l[i] != '9' and r[i] != '9' and u >= 1 + debit:
                u -= 1 + debit
                l[i] = '9'
                r[i] = '9'
            elif r[i] != '9' and u >= debit:
                r[i] = '9'
                u -= debit
            elif l[i] != '9' and u >= debit:
                l[i] = '9'
                u -= debit


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

