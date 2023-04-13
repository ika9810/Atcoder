# import sys
# input = sys.stdin.readline

# A, B = map(int, input().split())

# def cntt(a,b):
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
#     return a,b
# cnt = 0
# while(1):
#     if A == B:
#         exit(print(cnt))
#     else:
#         res = cntt(A,B)
#         A = res[0]
#         B = res[1]
#         cnt += 1
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def min_operations(a, b):
    gcd_val = gcd(a, b)
    a, b = a // gcd_val, b // gcd_val
    cnt = 0

    while a != b:
        if a > b:
            a, b = a - b, b
        else:
            a, b = a, b - a
        cnt += 1

    return cnt

A, B = map(int, input().split())
cnt = min_operations(A, B)
print(cnt)



