import sys

# We cache the number of moves to win a maze
cache = {}


def debug(*s):
    # pass
    print(*s, file=sys.stderr)


def split_horizontally_at(maze, i):
    # The row must be clear
    for c in maze[i]:
        if c == '#':
            return None

    top_maze = maze[:i]
    bot_maze = maze[i+1:]
    return top_maze, bot_maze


def split_vertically_at(maze, i):
    r = len(maze)

    # The col must be clear
    for k in range(r):
        if maze[k][i] == '#':
            return None

    lef_maze = [maze[k][:i] for k in range(r)]
    rig_maze = [maze[k][i+1:] for k in range(r)]
    return lef_maze, rig_maze


def get_nimber(mazes):
    return solve(mazes[0]) ^ solve(mazes[1])


def solve(maze):
    r = len(maze)
    if r == 0:
        return 0
    c = len(maze[0])
    if c <= 0:
        return 0

    cache_key = (''.join(maze), r)
    if cache_key in cache:
        return cache[cache_key]

    nimbers = set()

    # Horizontal splits
    for i in range(r):
        mazes = split_horizontally_at(maze, i)
        if mazes is not None:
            nimbers.add(get_nimber(mazes))

    # Vertical split
    for i in range(c):
        mazes = split_vertically_at(maze, i)
        if mazes is not None:
            nimbers.add(get_nimber(mazes))

    # Get lowest number not in nimbers
    mex = 0
    for i in range(len(nimbers) + 1):
        if i not in nimbers:
            mex = i
            break

    cache[cache_key] = mex
    return mex


def get_win_move_count(maze, r, c):
    win_move_count = 0
    for i in range(r):
        for j in range(c):

            # Horizontal split
            mazes = split_horizontally_at(maze, i)
            if mazes is not None:
                if get_nimber(mazes) == 0:
                    win_move_count += 1

            # Vertical split
            mazes = split_vertically_at(maze, j)
            if mazes is not None:
                if get_nimber(mazes) == 0:
                    win_move_count += 1

    return win_move_count


def main():
    t = int(input())
    for testcase_number in range(1, t + 1):
        r, c = map(int, input().split())
        maze = [input() for _ in range(r)]
        print('Case #{}: {}'.format(testcase_number, get_win_move_count(maze, r, c)))


if __name__ == '__main__':
    main()
