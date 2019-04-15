import sys

def debug(*s):
    pass
    #print(*s, file=sys.stderr)

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    debug()
    debug(s)
    if s[0] == 'S' and s[-1] == 'E':
        # Just go east and then south
        debug('ez')
        r = (['E'] * (n-1)) + (['S'] * (n-1))
    elif s[0] == 'E' and s[-1] == 'S':
        # Just go south and then east
        debug('ez')
        r = (['S'] * (n-1)) + (['E'] * (n-1))
    else:
        # First and last are the same, we need to find a spot to cross
        debug('complicated')
        first = s[0]
        target = 'E' if s[0] == 'S' else 'S'
        last = first
        h = 0
        for j in range(1, len(s)):
            if s[j] == target and last == target:
                break
            elif s[j] == target:
                h += 1
            last = s[j]
        debug('breaking through at', h)
        r = ([target] * h) + ([first] * (n-1)) + ([target] * (n-1-h))

    print('Case #{}:'.format(i+1), ''.join(r))
