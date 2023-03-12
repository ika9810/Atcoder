# 입력 받기
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# H가 1이거나 W가 1인 경우는 1가지 경우의 수만 가능하므로 1 출력
if H == 1 or W == 1:
    print(1)

else:
    # 방문한 칸의 숫자를 기록하는 집합
    visited = set()

    # 백트래킹 함수
    def backtrack(i, j, count):
        # (H, W)에 도달한 경우 가능한 경우의 수를 1 증가시킨 후 반환
        if i == H-1 and j == W-1:
            return count + 1

        # 현재 칸의 숫자를 방문한 칸의 집합에 추가
        visited.add(A[i][j])

        # 아래쪽 칸으로 이동할 수 있으면 이동하여 백트래킹
        if i < H-1 and A[i+1][j] not in visited:
            count = backtrack(i+1, j, count)

        # 오른쪽 칸으로 이동할 수 있으면 이동하여 백트래킹
        if j < W-1 and A[i][j+1] not in visited:
            count = backtrack(i, j+1, count)

        # 현재 칸의 숫자를 방문한 칸의 집합에서 제거
        visited.remove(A[i][j])

        # 가능한 경우의 수 반환
        return count

    # (1, 1)에서 출발하여 가능한 경우의 수 계산
    count = backtrack(0, 0, 0)

    # 가능한 경우의 수 출력
    print(count)
#By ChatGPT
