#!/bin/python3

import os

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    n = len(container)
    capacities = [0 for _ in range(0, n)]
    counts = [0 for _ in range(0,n) ]
    for i in range(0,n):
        for j in range(0, n):
            capacities[i] += container[i][j]
            counts[i] += container[j][i]
    
    capacities.sort()
    counts.sort()
    for i in range(0,n):
        if capacities[i] != counts[i]:
            return 'Impossible'
            
    return 'Possible'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
