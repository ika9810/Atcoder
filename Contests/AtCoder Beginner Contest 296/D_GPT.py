def check(X, N, M):
    count = 0
    for i in range(1, N + 1):
        count += min(X // i, N)
    return count >= M * 2


def smallest_integer(N, M):
    left = 1
    right = N * N + 1

    while left < right:
        mid = (left + right) // 2
        if check(mid, N, M):
            right = mid
        else:
            left = mid + 1

    if left == N * N + 1:
        return -1
    else:
        return left


def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    result = smallest_integer(N, M)
    print(result)


if __name__ == "__main__":
    main()
