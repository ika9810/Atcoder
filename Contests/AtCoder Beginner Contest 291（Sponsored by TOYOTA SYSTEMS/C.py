import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

x = 0
y = 0
visited = set([(0, 0)])

for i in range(N):
    if S[i] == "R":
        x += 1
    elif S[i] == "L":
        x -= 1
    elif S[i] == "U":
        y += 1
    elif S[i] == "D":
        y -= 1
    if (x, y) in visited:
        print("Yes")
        break

    visited.add((x, y))

else:
    print("No")
