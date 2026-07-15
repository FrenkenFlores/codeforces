n, k = tuple(map(int, input().split()))
o = list(map(int, input().split()))
x = 0
for i in range(n):
    if o[i] > 0 and o[i] >= o[k - 1]:
        x += 1
print(x)
