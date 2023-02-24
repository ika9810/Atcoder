import sys
input = sys.stdin.readline

S = list(input())[:-1]
cnt = 0
res = []
arr = ["A", "C", "G", "T"]
for i in range(len(S)):
    if S[i] in arr:
        cnt+=1
    else:
        res.append(cnt)
        cnt = 0
print(max(res))