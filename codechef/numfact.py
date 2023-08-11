def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
            factors.append(n)
    return factors

def ans(A):
    factors = {}
    for a in A:
        for f in prime_factors(a):
            factors[f] = factors[f] + 1 if f in factors else 1

    result = 1
    for count in factors.values():
        result = (count + 1) * result

    return result

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        input()
        A = list(map(int, input().rstrip().split()))
        print(ans(A))
