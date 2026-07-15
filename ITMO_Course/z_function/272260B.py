n = int(input())
for _ in range(n):
    d = {}
    m = 0
    s = input()
    for i in range(len(s)):
        suffix = s[:i]
        prefix = s[-i:]
        if suffix == prefix or not suffix or not prefix:
            continue
        d[suffix] = 0
        d[prefix] = 0
    for e in d.keys():
        for j in range(len(s)):
            if s[j:j+len(e)] == e:
                d[e] += 1
    print(sum(list(d.values())))
