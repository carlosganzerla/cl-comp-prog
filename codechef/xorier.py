mask = 2**32 - 2**2

def combine(n):
    if n > 1:
        return (n * (n - 1)) // 2
    return 0

def ans(A):
    odd = [a for a in A if a % 2 == 1]
    even = [a for a in A if a % 2 == 0]
    result = 0

    even_duplicates = {}
    for e in even:
        masked = mask & e
        even_duplicates[masked] = even_duplicates[masked] + 1 if masked in even_duplicates else 1

    odd_duplicates = {}
    for o in odd:
        masked = mask & o
        odd_duplicates[masked] = odd_duplicates[masked] + 1 if masked in odd_duplicates else 1

    n_odd = len(odd)
    n_even = len(even)
    result += combine(n_odd)
    result += combine(n_even)
    for n in odd_duplicates.values():
        result -= combine(n)

    for n in even_duplicates.values():
        result -= combine(n)

    return result

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        N = int(input().rstrip())
        A = list(map(int, input().rstrip().split()))
        print(ans(A))
