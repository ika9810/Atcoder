import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

count = 2*N

for _ in range(N):
    X.remove(min(X))
    X.remove(max(X))
sum = 0
for i in range(len(X)):
    sum+= X[i]
print(sum/len(X))