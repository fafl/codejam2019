t = int(input())
for i in range(t):
    n = input()
    s1 = ''
    s2 = ''
    for j in range(len(n)):
        if n[j] == '4':
            s1 += '3'
            s2 += '1'
        else:
            s1 += n[j]
            s2 += '0'
    print('Case #{}:'.format(i+1), int(s1), int(s2))
