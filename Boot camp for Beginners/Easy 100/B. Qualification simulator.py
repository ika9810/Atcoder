import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())
S = list(input())[:-1]

cnt = A + B
over = 0
for i in range(len(S)):
    if S[i] == "c":
        print("No")
    elif S[i] == "a":
        if  cnt > 0:
            cnt -= 1
            print("Yes")
        else:
            print("No")
    elif S[i] == "b":
        if  cnt > 0:
            if over <= B:
                over += 1
                cnt -= 1
                print("Yes")
            else:
                pass
        else:
            print("No")
    else:
        pass