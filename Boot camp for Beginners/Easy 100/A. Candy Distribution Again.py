import sys
input = sys.stdin.readline
N, x = map(int,input().split())

a = list(map(int, input().split()))
a. sort()
sum = 0
cnt = 0
for i in range(len(a)):
    sum += a[i]
    if sum < x:
        cnt += 1
    elif sum == x:
        cnt += 1
        exit(print(cnt))
    else:
        exit(print(cnt))
print(cnt-1)