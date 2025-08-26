# 입력 받기
N = int(input())
grid = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

# 방향: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    stack = [(x, y)]
    visited[x][y] = True
    count = 1

    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                    count += 1
    return count

# 단지 수와 집 수 계산
complexes = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visited[i][j]:
            house_count = dfs(i, j)
            complexes.append(house_count)

# 출력
complexes.sort()
print(len(complexes))
for count in complexes:
    print(count)
