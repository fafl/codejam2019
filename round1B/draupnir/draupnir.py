import sys


def debug(*s):
    # pass
    print(*s, file=sys.stderr)


def main():
    t, f = map(int, input().split())

    # R values need 7 bits at most, as each R is less than 128
    # R values will shift to the left at different speeds. At some point they will no longer overlap.
    # We need to find the first day where R4, R5 and R6 are far enough apart
    # This will find 185
    r4start = 6
    r5start = 6
    r6start = 6
    r4r5r6_day = 0
    while True:
        r4r5r6_day += 1
        if r4r5r6_day % 4 == 0:
            r4start += 1
        if r4r5r6_day % 5 == 0:
            r5start += 1
        if r4r5r6_day % 6 == 0:
            r6start += 1
        if 7 <= r4start - r5start and 7 <= r5start - r6start:
            break

    # Find the first day where r1, r2 and r3 are far enough apart
    # This will find 38
    r1start = 6
    r2start = 6
    r3start = 6
    r1r2r3_day = 0
    while True:
        r1r2r3_day += 1
        if r1r2r3_day % 1 == 0:
            r1start += 1
        if r1r2r3_day % 2 == 0:
            r2start += 1
        if r1r2r3_day % 3 == 0:
            r3start += 1
        if 7 <= r1start - r2start and 7 <= r2start - r3start:
            break

    for testcase_number in range(1, t + 1):

        # Send the day to get r4, r5 and r6
        print(r4r5r6_day, flush=True)
        response = int(input())

        # Find r4, r5 and r6 in the response
        binary_response = '0' * 100 + bin(response)[2:]
        r4 = int(binary_response[-r4start-1:-r4start+6], 2)
        r5 = int(binary_response[-r5start-1:-r5start+6], 2)
        r6 = int(binary_response[-r6start-1:-r6start+6], 2)

        # Send the day to get r1, r2 and r3
        print(r1r2r3_day, flush=True)
        response = int(input())

        # A part of this response is r4, r5 and r6. We need to remove them.
        response -= r4 * (2 ** (r1r2r3_day // 4))
        response -= r5 * (2 ** (r1r2r3_day // 5))
        response -= r6 * (2 ** (r1r2r3_day // 6))

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
