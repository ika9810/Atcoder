import sys
input = sys.stdin.readline

N,D = map(int, input().split())
T = list(map(int,input()[:-1].split(" ")))

for i in range(len(T)-1):
    if T[i+1] - T[i] <= D:
        exit(print(T[i+1]))
else:
    print(-1)