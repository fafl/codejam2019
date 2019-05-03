import sys


def debug(*s):
    # pass
    print(*s, file=sys.stderr)


def solve(p, q, people):
    # debug('---')
    walk_ns = []
    walk_ew = []

    south_counter = 0
    west_counter = 0
    for person in people:
        x, y, direction = person.split()
        if direction in 'NS':
            is_north = direction == 'N'
            walk_ns.append((int(y) + (1 if is_north else 0), is_north))
            if not is_north:
                south_counter += 1
        else:
            is_east = direction == 'E'
            walk_ew.append((int(x) + (1 if is_east else 0), is_east))
            if not is_east:
                west_counter += 1

    walk_ns.sort(key=lambda t: (t[0], t[1]))
    highest_y = south_counter
    highest_y_at = 0
    current = south_counter
    for c, is_north in walk_ns:
        if is_north:
            current += 1
            if highest_y < current:
                highest_y = current
                highest_y_at = c
        else:
            current -= 1

    walk_ew.sort(key=lambda t: (t[0], t[1]))
    highest_x = west_counter
    highest_x_at = 0
    current = west_counter
    for c, is_east in walk_ew:
        if is_east:
            current += 1
            if highest_x < current:
                highest_x = current
                highest_x_at = c
        else:
            current -= 1

    return highest_x_at, highest_y_at


def main():
    t = int(input())
    for testcase_number in range(1, t + 1):
        p, q = map(int, input().split())
        people = [input() for _ in range(p)]
        x, y = solve(p, q, people)

        print('Case #{}: {} {}'.format(testcase_number, x, y))


if __name__ == '__main__':
    main()
