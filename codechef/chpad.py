from math import gcd

def ans(A, B):
    mod = A % B
    if mod == 0:
        return "Yes"
    gc = gcd(A, B)
    if gc == 1:
        return "No"
    return ans(A, B // gc)

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        A, B = tuple(map(int, input().rstrip().split()))
        print(ans(A, B))
