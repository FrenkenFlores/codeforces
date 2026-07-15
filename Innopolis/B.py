from collections import OrderedDict


n = int(input())
for _ in range(n):
    p1, p2 = map(list, input().split("+"))
    if p1 and not p2:
        print(''.join(p1))
        continue
    elif p2 and not p1:
        print(''.join(p2))
        continue
    s = ''
    c = set(p1 + p2)
    for i in c:
        if p1.count(i) > p2.count(i):
            for j in range(p1.count(i), 0, -1):
                if j == p2.copy().count(i):
                    s += i * j
                    for _ in range(j):
                        p1.remove(i)
                        p2.remove(i)
                    if not p1 and not p2:
                        s += '2'
        else:
            for j in range(p2.count(i), 0, -1):
                if j == p1.copy().count(i):
                    s += i * j
                    for _ in range(j):
                        p1.remove(i)
                        p2.remove(i)
                    if not p1 and not p2:
                        s += '2'
    if p1:
        p1 = ''.join(sorted(p1))
    if p2:
        p2 = ''.join(sorted(p2))
    s = ''.join(sorted(s))
    s_dict = OrderedDict()
    p1_dict = OrderedDict()
    p2_dict = OrderedDict()

    for i in s:
        if i not in s_dict:
            s_dict[i] = 1
        else:
            s_dict[i] += 1
    s = ''
    for i in s_dict:
        if s_dict[i] > 1:
            s += f'{i}{s_dict[i]}'
        else:
            s += i

    for i in p1:
        if i not in p1_dict:
            p1_dict[i] = 1
        else:
            p1_dict[i] += 1
    p1 = ''
    for i in p1_dict:
        if p1_dict[i] > 1:
            p1 += f'{i}{p1_dict[i]}'
        else:
            p1 += i
    for i in p2:
        if i not in p2_dict:
            p2_dict[i] = 1
        else:
            p2_dict[i] += 1

    p2 = ''
    for i in p2_dict:
        if p2_dict[i] > 1:
            p2 += f'{i}{p2_dict[i]}'
        else:
            p2 += i

    if not p1 and p2:
        p1 = '1'
    elif not p2 and p1:
        p2 = '1'
    elif not p1 and not p2:
        p1 = ''
        p2 = ''
    o = ''
    if s and p1 and p2:
        o = f'{s}({p1}+{p2})'
    elif not s and p1 and p2:
        o = f'{p1}+{p2}'
    elif not p1 and not p2 and s:
        o = f'{s}'
    print(o)
