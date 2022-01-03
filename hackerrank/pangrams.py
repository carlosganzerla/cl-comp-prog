#!/bin/python3

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    letters = {}
    for i in range(0, len(s)):
        letter = s[i].lower()
        if letter not in letters:
            letters[letter] = True

    return len(letters) == 27

    # Write your code here

if __name__ == '__main__':
    s = input()

    result = pangrams(s)

    print('pangram' if result else 'not pangram')
