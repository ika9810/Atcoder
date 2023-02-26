import sys
input = sys.stdin.readline
S = input()
for i in range(len(S)):
    if ord(S[i]) >= 65 and ord(S[i]) <= 90:
        exit(print(i+1))