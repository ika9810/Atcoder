import sys
input = sys.stdin.readline

N, X  = map(int, input().split())
A = list(map(int, list(input().split())))
if X == 0:
    exit(print("Yes"))
else:
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i] - A[j] == X:
                exit(print("Yes"))
    else:
        print("No")