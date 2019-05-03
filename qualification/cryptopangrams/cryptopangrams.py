import sys


def debug(*s):
    pass
    # print(*s, file=sys.stderr)


def main():
    t = int(input())
    for testcase_number in range(1, t + 1):
        n, l = map(int, input().split())
        encrypted = [int(x) for x in input().split()]
        debug()
        debug(n, l)
        debug(encrypted)

        # Find smallest
        smallest = 999999999999999
        smallest_at = -1
        for i in range(len(encrypted)):
            if encrypted[i] < smallest:
                smallest = encrypted[i]
                smallest_at = i

        # Factor the smallest
        for factor in range(2, int(smallest ** 0.5) + 1):
            if smallest % factor == 0:
                break

        # First number found, check if it's left or right
        ciphered = [None] * (len(encrypted) + 1)
        if smallest_at + 1 < len(encrypted) and encrypted[smallest_at + 1] % factor == 0:
            start_from = smallest_at + 1
        else:
            start_from = smallest_at
        ciphered[start_from] = factor

        # Fill "ciphered", go left
        for i in range(start_from + 1, len(ciphered)):
            ciphered[i] = encrypted[i-1] // ciphered[i-1]

        # Fill "ciphered", go right
        for i in range(start_from - 1, -1, -1):
            ciphered[i] = encrypted[i] // ciphered[i+1]

        # Create the mapping
        m = list(sorted(set(ciphered)))
        letter_of_prime = {x: chr(i + 65) for i, x in enumerate(m)}

        debug(ciphered)
        debug(letter_of_prime)

        print('Case #{}:'.format(testcase_number), ''.join(letter_of_prime[x] for x in ciphered))


if __name__ == '__main__':
    main()
