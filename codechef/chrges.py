OPPOSITES = {
    "-": "+",
    "+": "-",
}

def ans(S):
    result = 0
    current_charge = None
    contiguous = 0
    for s in S:
        if current_charge is None and s in ["-", "+"]:
            current_charge = s
        elif current_charge is not None and s == OPPOSITES[current_charge]:
            result += contiguous % 2
            current_charge = s
            contiguous = 0
        elif current_charge is not None and s == current_charge:
            contiguous = 0
        elif current_charge is not None and s == "0":
            contiguous += 1

    return result if current_charge is not None else len(S)

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        input()
        print(ans(input()))
