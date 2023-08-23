import random

MAX_BITS = 20

def gen_random():
    ones = random.randint(0, MAX_BITS // 2) * 2
    bit_array = []
    for i in range(0, MAX_BITS):
        if i < MAX_BITS - ones:
            n = int(random.randint(1, MAX_BITS) <= ones)
            bit_array.append(str(n))
            ones -= n
        else:
            bit_array.append(str(1))
            ones -= 1


    if ones > 0:
        raise Exception("fail")

    return int(''.join(bit_array), 2)

def generate(N):
    count = 0
    generated = set()
    while count < N:
        n = gen_random()
        if n in generated:
            continue

        generated.add(n)
        yield n
        count += 1


if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        N = int(input().rstrip())
        print(*generate(N))
