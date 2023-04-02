import sys
input = sys.stdin.readline

for i in range(8):
    S = list(input())[:-1]
    if "*" in S:
        res = S.index("*")
        print(str(chr(res+97)) + str(8 - i))