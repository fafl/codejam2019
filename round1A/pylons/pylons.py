import sys


def debug(*s):
    pass
    #print(*s, file=sys.stderr)


def get_all_diagonals(board):
    r = len(board)
    c = len(board[0])

    fdiag = [[] for _ in range(r + c - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -r + 1

    for x in range(c):
        for y in range(r):
            fdiag[x + y].append((y, x))
            bdiag[x - y - min_bdiag].append((y, x))

    return fdiag + bdiag


def solve(board, last_x, last_y, level=0):
    r = len(board)
    c = len(board[0])

    # Base case
    for y in range(r):
        if not all(board[y]):
            debug('Not all filled')
            for i in range(r):
                debug(board[i])
            break
    else:
        return []

    # Order unfilled fields by number of unfilled neighbors
    unfilled_neighbor_count = []
    for _ in range(r):
        unfilled_neighbor_count.append([0] * c)

    # Horizontal
    for i in range(r):
        unfilled_count = sum(1 for j in range(c) if not board[i][j])
        for j in range(c):
            unfilled_neighbor_count[i][j] += unfilled_count - 1

    # Vertical
    for j in range(c):
        unfilled_count = sum(1 for i in range(r) if not board[i][j])
        for i in range(r):
            unfilled_neighbor_count[i][j] += unfilled_count - 1

    # Diagonals
    for diagonal in get_all_diagonals(board):
        unfilled_count = sum(1 for i, j in diagonal if not board[i][j])
        for i, j in diagonal:
            unfilled_neighbor_count[i][j] += unfilled_count - 1

    # Try them all
    coordinates_by_unfilled_count = [(y, x) for y in range(r) for x in range(c)]
    coordinates_by_unfilled_count.sort(key=lambda t: unfilled_neighbor_count[t[0]][t[1]], reverse=True)
    for y, x in coordinates_by_unfilled_count:
        if board[y][x]:
            # Field already full
            continue
        if x == last_x or y == last_y or x + y == last_x + last_y or x - y == last_x - last_y:
            # Last field blocks this field
            continue
        board[y][x] = True
        debug(' '*level + 'Trying', x, y)
        solution = solve(board, x, y, level+1)
        if solution is not None:
            return [(y, x)] + solution
        board[y][x] = False

    return None


def main():
    t = int(input())
    for testcase_number in range(1, t + 1):

        r, c = map(int, input().split())
        debug('will work on', r, c)

        board = []
        for _ in range(r):
            board.append([False] * c)

        solution = solve(board, -1, -2)
        if solution is None:
            print('Case #{}: IMPOSSIBLE'.format(testcase_number))
        else:
            print('Case #{}: POSSIBLE'.format(testcase_number))
            for x, y in solution:
                print(x + 1, y + 1)


if __name__ == '__main__':
    main()
