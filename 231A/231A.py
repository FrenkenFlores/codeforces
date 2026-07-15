n = int(input())
i = 0
for _ in range(n):
    m = map(int, input().split())
    m = list(filter(lambda x: bool(x), m))
    if len(m) > 1:
        i += 1
print(i)
    
