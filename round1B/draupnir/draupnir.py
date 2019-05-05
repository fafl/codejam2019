import sys


def debug(*s):
    # pass
    print(*s, file=sys.stderr)


def main():
    t, f = map(int, input().split())

    for testcase_number in range(1, t + 1):

        # R values need 7 bits at most, each R is less than 128
        # First we need to find a day where R4, R5 and R6 are far enough apart
        r4start = 6
        r5start = 6
        r6start = 6
        i = 0
        while True:
            i += 1
            if i % 4 == 0:
                r4start += 1
            if i % 5 == 0:
                r5start += 1
            if i % 6 == 0:
                r6start += 1
            if 7 <= r4start - r5start and 7 <= r5start - r6start:
                break

        print(i, flush=True)
        response = int(input())

        # Find r4, r5 and r6 in the response
        binary_response = '0' * 100 + bin(response)[2:]
        r4 = int(binary_response[-r4start-1:-r4start+6], 2)
        r5 = int(binary_response[-r5start-1:-r5start+6], 2)
        r6 = int(binary_response[-r6start-1:-r6start+6], 2)

        # Find a day where r1, r2 and r3 are far enough apart
        r1start = 6
        r2start = 6
        r3start = 6
        i = 0
        while True:
            i += 1
            if i % 1 == 0:
                r1start += 1
            if i % 2 == 0:
                r2start += 1
            if i % 3 == 0:
                r3start += 1
            if 7 <= r1start - r2start and 7 <= r2start - r3start:
                break

        print(i, flush=True)
        response = int(input())

        # A part of this response is r4, r5 and r6, we need to remove it
        response -= r4 * (2 ** (i // 4))
        response -= r5 * (2 ** (i // 5))
        response -= r6 * (2 ** (i // 6))

        # Find r1, r2 and r3 in the response
        binary_response = '0' * 100 + bin(response)[2:]
        r1 = int(binary_response[-r1start-1:-r1start+6], 2)
        r2 = int(binary_response[-r2start-1:-r2start+6], 2)
        r3 = int(binary_response[-r3start-1:-r3start+6], 2)

        # All done
        print(r1, r2, r3, r4, r5, r6, flush=True)

        assert input()


if __name__ == '__main__':
    main()
