import sys

input = sys.stdin.readline

S = input().split("\n")[0]
arr = ["0"]*len(S) 

for i in range(1, len(S)//2 + 1):
    arr[2*i-1] = S[2*i - 2]
    arr[2*i - 2] = S[2*i -1 ]
print("".join(arr))

