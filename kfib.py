n, k = input().split()
n = int(n)
k = int(k)

vec = [ 1 for _ in range(n) ]

current = k

for i in range(k, n):
    j = 0
    vec[i] = current
    current = (2 * current - vec[j]) % 1000000007
    j += 1

print(vec[n-1])
