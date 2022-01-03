#!/bin/python3

# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.

squares = [
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
]


def ans(s):
    rng = range(0,3)
    cost = 999

    for square in squares:
        current_cost = 0
        for i in rng:
            for j in rng:
                current_cost += abs(square[i][j] - s[i][j])

        if current_cost < cost:
            cost = current_cost

    return cost
# Write your code here

if __name__ == '__main__':
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = ans(s)

    print(result)

