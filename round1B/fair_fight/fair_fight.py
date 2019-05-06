import sys

# This code currently does not solve the large testset, it causes a TLE


def debug(*s):
    # pass
    print(*s, file=sys.stderr)


class RMQ:

    def __init__(self, a, f):
        self.a = a
        self.f = f
        self.precomputed = [[x] for x in range(len(a))]
        for exp in range(len(a).bit_length() - 1):
            for i in range(len(a)):
                p1 = self.precomputed[i][exp]
                p2 = self.precomputed[min(len(a)-1, i+2**exp)][exp]
                p = p1 if f(a[p1], a[p2]) == a[p1] else p2
                self.precomputed[i].append(p)

    def get_f_index(self, i1, i2):
        # i1 is inclusive, i2 is exclusive
        difflen = (i2 - i1).bit_length() - 1
        p1 = self.precomputed[i1][difflen]
        p2 = self.precomputed[i2-2**difflen][difflen]
        p = p1 if self.f(self.a[p1], self.a[p2]) == self.a[p1] else p2
        return p

    """
    def selftest(self):
        import random
        for i in range(100):
            a = [random.randrange(20) for _ in range(50)]
            rmq = RMQ(a, max)
            for i1 in range(49):
                for i2 in range(i1+1, 50):
                    rmq_result = rmq.get_f_index(i1, i2)
                    correct_result = max(range(i1, i2), key=lambda x: a[x])
                    if rmq_result != correct_result:
                        print(a)
                        print('result from {} to {} is {} but should be {}'.format(
                            i1, i2, rmq_result, correct_result
                        ))
                        print('=======')
        print('selftest done')
    """


def bin_search(a, predicate, leftmost=True, lo=0, hi=None):
    # Returns the index of the leftmost element that fulfills the predicate
    # This only works if the input array is sorted:
    # * Elements that fulfill the predicate are on the left side, elements that do not are on the other
    # Setting leftmost=False flips this
    # lo is inclusive, hi is exclusive
    if hi is None:
        hi = len(a) - 1
    else:
        hi -= 1
    if leftmost and not predicate(hi):
        return None
    if not leftmost and not predicate(lo):
        return None
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if predicate(mid):
            if leftmost:
                hi = mid
            else:
                lo = mid
        else:
            if leftmost:
                lo = mid + 1
            else:
                hi = mid - 1
    if lo == hi:
        return lo
    else:
        if leftmost:
            return lo if predicate(lo) else hi
        else:
            return hi if predicate(hi) else lo


def solve(n, k, c, d):
    c_rmq = RMQ(c, max)
    d_rmq = RMQ(d, max)

    # Divide and Conquer with BFS:
    # * First find the max element in C and find all intervals that include it
    # * Then check the left and right side
    queue = [(0, n)]
    interval_count = 0
    while queue:
        lo, hi = queue.pop()

        if hi <= lo:
            continue

        # Find index of max element in C
        i = c_rmq.get_f_index(lo, hi)

        # Add left and right sides to queue
        queue.append((lo, i))
        queue.append((i + 1, hi))

        # From the official analysis:
        # * p1 means: (best sword in C for given L and R) is at i
        # * p2 means: (best sword in D for given L and R) <= Ci + K
        # * p3 means: (best sword in D for given L and R) + K < Ci
        # p1 is already fulfilled

        # Find leftmost index where p2 is still valid
        leftmost_p2 = bin_search(
            c,
            lambda idx: (
                d[d_rmq.get_f_index(idx, i + 1)] <= c[i] + k
            ),
            leftmost=True,
            lo=lo,
            hi=i + 1
        )
        if leftmost_p2 is None:
            continue

        # Find rightmost index where p2 is still valid
        rightmost_p2 = bin_search(
            c,
            lambda idx: (
                d[d_rmq.get_f_index(i, idx + 1)] <= c[i] + k
            ),
            leftmost=False,
            lo=i,
            hi=hi
        )
        if rightmost_p2 is None:
            continue

        # Find leftmost index where p3 is still valid
        leftmost_p3 = bin_search(
            c,
            lambda idx: (
                d[d_rmq.get_f_index(idx, i + 1)] + k < c[i]
            ),
            leftmost=True,
            lo=lo,
            hi=i + 1
        )

        # Find rightmost index where p3 is still valid
        rightmost_p3 = bin_search(
            c,
            lambda idx: (
                d[d_rmq.get_f_index(i, idx + 1)] + k < c[i]
            ),
            leftmost=False,
            lo=i,
            hi=hi
        )

        # Count intervals for p1 and p2
        interval_count += (i - leftmost_p2 + 1) * (rightmost_p2 - i + 1)

        # Count intervals for p1 and p3
        if leftmost_p3 is not None and rightmost_p3 is not None:
            interval_count -= (i - leftmost_p3 + 1) * (rightmost_p3 - i + 1)

    return interval_count


def main():

    # Tests with random data
    # TODO

    t = int(input())
    for testcase_number in range(1, t + 1):
        n, k = map(int, input().split())
        c = list(map(int, input().split()))
        d = list(map(int, input().split()))
        print('Case #{}: {}'.format(testcase_number, solve(n, k, c, d)))


if __name__ == '__main__':
    main()
