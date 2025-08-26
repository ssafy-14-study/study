from collections import deque

def BFS(i, j, rain, arr, visited, N):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] > rain and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_h = max(map(max, arr))

answer = 0
# 강수량 0부터 시작 (비가 안 올 수도 있음)
for rain in range(0, max_h+1):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > rain and not visited[i][j]:
                BFS(i, j, rain, arr, visited, N)
                cnt += 1
    answer = max(answer, cnt)

print(answer)
