# K Q R R B B N N
import sys
input = sys.stdin.readline

S = list(input())[:-1]
one = list(filter(lambda x: S[x] == "B", range(len(S))))

rest_list = list(filter(lambda x: S[x] == "R", range(len(S))))
kk = S.index("K")
if rest_list[0] < kk < rest_list[1]:
    if (one[0]%2) != (one[1]%2):
        exit(print("Yes"))
    else:
        exit(print("No"))
else:
    print("No")