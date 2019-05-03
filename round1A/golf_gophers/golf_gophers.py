def find_first(rests):
    prev, candidate = rests[0]
    for divisor, remainder in rests[1:]:
        while candidate % divisor != remainder:
            candidate += prev
        prev *= divisor
    return candidate


def main():
    t, n, m = map(int, input().split())

    for testcase_number in range(1, t + 1):
        rests = []
        for f in [17, 16, 13, 11, 9, 7, 5]:
            print(*[f for _ in range(18)], flush=True)
            remainder = sum(int(x) for x in input().split()) % f
            rests.append((f, remainder))

        print(find_first(rests), flush=True)
        success = int(input())
        if success < 0:
            break


if __name__ == '__main__':
    main()
