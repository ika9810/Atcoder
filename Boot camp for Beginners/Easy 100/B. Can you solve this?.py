import sys
input = sys.stdin.readline

N, M, C = map(int, input().split())
B = list(map(int, input().split()))

cnt = 0
for i in range(N):
    A = list(map(int, input().split()))
    sum = 0
    for j in range(len(A)):
        sum += A[j]*B[j]
    if sum + C > 0:
        cnt+=1
    else:
        pass
print(cnt)