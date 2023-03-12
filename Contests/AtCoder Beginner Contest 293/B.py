import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
arr = [0]*N
res = ""
cnt = 0
for i in range(len(arr)):
    if arr[i] == 0:
        arr[A[i]-1] = 1
    elif arr[i] != 0:
        pass
for j in range(len(arr)):
    if arr[j] == 0:
        cnt+=1
        res += str(j+1) + " "
print(cnt)
print(res[:-1])