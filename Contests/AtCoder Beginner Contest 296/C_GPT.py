def find_pair_with_difference(N, X, A):
    if X == 0:
        return "Yes"

    unique_numbers = set(A)

    for num in unique_numbers:
        if num + X in unique_numbers:
            return "Yes"

    return "No"


def main():
    import sys
    input = sys.stdin.readline

    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    result = find_pair_with_difference(N, X, A)
    print(result)


if __name__ == "__main__":
    main()