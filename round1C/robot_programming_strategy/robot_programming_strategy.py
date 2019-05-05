import sys

BEATEN_BY = {
    'R': 'S',
    'P': 'R',
    'S': 'P'
}


def debug(*s):
    # pass
    print(*s, file=sys.stderr)


def solve(bots):

    # Make bot programs longer
    alive_bots = bots[:]
    for i in range(len(alive_bots)):
        while len(alive_bots[i]) < 256:
            alive_bots[i] *= 2

    # Fight against all bots at the same time
    result = ''
    for i in range(256):
        bot_moves = set(b[i] for b in alive_bots)
        move = None
        if len(bot_moves) == 3:
            return None
        elif len(bot_moves) == 2:
            if 'P' not in bot_moves:
                move = 'R'
            elif 'S' not in bot_moves:
                move = 'P'
            else:
                move = 'S'
        elif len(bot_moves) == 1:
            if 'P' in bot_moves:
                move = 'S'
            elif 'S' in bot_moves:
                move = 'R'
            else:
                move = 'P'

        result += move
        alive_bots = [b for b in alive_bots if b[i] != BEATEN_BY[move]]
        if not alive_bots:
            break

    return result


def main():
    t = int(input())
    for testcase_number in range(1, t + 1):

        a = int(input())
        bots = [input() for _ in range(a)]

        solution = solve(bots)
        if solution is None:
            print('Case #{}: IMPOSSIBLE'.format(testcase_number))
        else:
            print('Case #{}: {}'.format(testcase_number, solution))


if __name__ == '__main__':
    main()
