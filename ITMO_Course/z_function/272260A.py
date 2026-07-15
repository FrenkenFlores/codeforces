t = int(input())
for _ in range(t):
    s = input()
    for i in range(len(s), 0, -1):
        j = s[:i]
        if j == j[i::-1]:
            print(i)
            break
