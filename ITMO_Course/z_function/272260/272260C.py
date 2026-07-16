q = int(input())
for _ in range(q):
    t = input()
    p = input()
    idx = []
    for i in range(len(t)-len(p)+1):
        c = list(p)
        while True:
            try:
                j = c.index('?')
            except ValueError:
                break
            c[j] = t[i:i+len(p)][j]
        c = ''.join(c)
        if c == t[i:i+len(p)]:
            idx.append(str(i))
    print(len(idx))
    print(" ".join(idx))
