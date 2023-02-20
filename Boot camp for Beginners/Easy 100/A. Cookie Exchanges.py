import sys
input = sys.stdin.readline

A, B, C = map(int,input().split())
if A % 2 != 0 or C % 2 != 0 or B % 2 != 0:
    print(0)
else:
    if A == B == C:
        print(-1)
    else:
        a = A
        b = B
        c = C
        cnt = 0
        while(1):
            if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
                print(cnt)
                break
            if a == b == c:
                print(cnt)
                break
            divide_a = a//2
            divide_b = b//2
            divide_c = c//2
            a = divide_b + divide_c
            b = divide_a + divide_c
            c = divide_a + divide_b
            
            cnt+=1
            