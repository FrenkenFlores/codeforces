# Get input
W, H, x, y, w, h = tuple(map(int, input().split()))
T = input()

# Create grid
m = [[' ' for i in range(W)] for j in range(H)]

# Make outer border
m[0][0] = '+'
m[0][W - 1] = '+'
m[H - 1][0] = '+'
m[H - 1][W - 1] = '+'
for i in range(1, H - 1):
    m[i][0] = '|'
    m[i][W - 1] = '|'
for i in range(1, W - 1):
    m[0][i] = '-'
    m[H - 1][i] = '-'

# Fill inner screen
for i in range(h):
    for j in range(w):
        m[y - 1 + i][x - 1 + j] = "."

# Make inner border
m[y - 1 + 0][x - 1 + 0] = '+'
m[y - 1 + 0][x - 1 + w - 1] = '+'
m[y - 1 + h - 1][x - 1 + 0] = '+'
m[y - 1 + h - 1][x - 1 + w - 1] = '+'
for i in range(1, h - 1):
    m[y - 1 + i][x - 1 + 0] = '|'
    m[y - 1 + i][x - 1 + w - 1] = '|'
for i in range(1, w - 1):
    m[y - 1 + 0][x - 1 + i] = '_'
    m[y - 1 + h - 1][x - 1 + i] = '-'

# Add program name
for i, j in zip(range(len(m[y - 1])), T):
    m[y - 1][x - 1 + i] = j

# Add control panel
for i, j in zip(
    range(
        x + w - 2,
        0,
        -1
    ),
    'XO-'
):
    m[y - 1][i] = j

# Print screen
for i in range(len(m)):
    for j in range(len(m[0])):
        print(m[i][j], end='')
    print()
