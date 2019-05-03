import sys


def debug(*s):
    # pass
    print(*s, file=sys.stderr)


def get_missing_indices(responses, n):
    missing_indices = []
    for candidate in range(n):
        i = candidate - len(missing_indices)
        if len(responses[0]) <= i:
            missing_indices.append(candidate)
            continue
        if int(responses[0][i]) != candidate % 2:
            missing_indices.append(candidate)
            continue
        if int(responses[1][i]) != (candidate // 2) % 2:
            missing_indices.append(candidate)
            continue
        if int(responses[2][i]) != (candidate // 4) % 2:
            missing_indices.append(candidate)
            continue
        if int(responses[3][i]) != (candidate // 8) % 2:
            missing_indices.append(candidate)
            continue
        if int(responses[4][i]) != (candidate // 16) % 2:
            missing_indices.append(candidate)
            continue

    return missing_indices


def main():
    t = int(input())

    for testcase_number in range(1, t + 1):
        n, b, f = map(int, input().split())

        responses = []
        for exp in range(5):
            zeros = '0' * (2 ** exp)
            ones = '1' * (2 ** exp)
            request = ''
            while len(request) < n:
                request += zeros
                request += ones
            print(request[:n], flush=True)
            responses.append(input())

        print(*get_missing_indices(responses, n), flush=True)
        assert 0 < int(input())


if __name__ == '__main__':
    main()
