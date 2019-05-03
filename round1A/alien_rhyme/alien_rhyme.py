import sys


def debug(*s):
    # pass
    print(*s, file=sys.stderr)


def count_overlapping_pairs(node):
    visit_counter, children = node
    child_counters = sum(count_overlapping_pairs(c) for c in children.values())
    pairs_from_this = 0 if visit_counter - child_counters < 2 else 2
    return pairs_from_this + child_counters


def solve(words):
    words = [list(reversed(w)) for w in words]

    trie = {}
    for word in words:
        node = trie
        for c in word:
            if c not in node:
                node[c] = [0, {}]   # counter and children
            node[c][0] += 1
            node = node[c][1]

    return sum(count_overlapping_pairs(node) for node in trie.values())


def main():
    t = int(input())
    for testcase_number in range(1, t + 1):
        n = int(input())
        words = [input() for _ in range(n)]

        print('Case #{}: {}'.format(testcase_number, solve(words)))


if __name__ == '__main__':
    main()
