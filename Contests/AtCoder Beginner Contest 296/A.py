import sys
input = sys.stdin.readline

N = int(input())
S = list(input())[:-1]

if len(S) == 1:
    exit(print("Yes"))
else:
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            exit(print("No"))
    else:
        print("Yes") 