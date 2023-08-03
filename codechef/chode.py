def ans(encrypted: str, plain_freq: str):
    freq_map = {}
    for char in encrypted:
        if not char.isalpha():
            continue
        if char.lower() in freq_map:
            freq_map[char.lower()] += 1
        else:
            freq_map[char.lower()] = 1

    cypher_freq = sorted(freq_map, key=lambda char: (freq_map[char], char))
    translator: dict[str, str] = {}
    for i in range(0, len(cypher_freq)):
        translator[cypher_freq[i]] = plain_freq[len(plain_freq) - len(cypher_freq) + i]

    result: list[str] = []
    for i in range(0, len(encrypted)):
        char = encrypted[i]
        if char.isalpha():
            appended = translator[char.lower()] if char.islower() else translator[char.lower()].upper()
            result.append(appended)
        else:
            result.append(char)

    return ''.join(result)


if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(0, T):
        plain_freq = input()
        encrypted = input()
        print(ans(encrypted, plain_freq))
