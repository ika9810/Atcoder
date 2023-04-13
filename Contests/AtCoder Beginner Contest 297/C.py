import sys
input = sys.stdin.readline
res = []
H, W = map(int,input().split())
for _ in range(H):
    S = list(input()[:-1])
    #print(S)
    for i in range(len(S)-1):
        #print(S,i)
        if S[i] == "T":
            if S[i + 1] == "T":
                S[i] = "P"
                S[i+1] = "C"
    res.append("".join(S))
for k in res:
    print(k)