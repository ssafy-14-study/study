# 주변에 높은게 있으면 return
# 같으면 스택에 append
# 주변에 낮은 것만 있으면 + 1

def dfs(s_i, s_j):
    global cnt
    stack = []
    stack.append((s_i, s_j))
    visited[s_i][s_j] = True

    while stack:
        (vi, vj) = stack.pop()
        # 8방향 델타
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            new_i = vi + di
            new_j = vj + dj
            # 델타 중 arr[vi][vj] 보다 큰 것이 있으면 return
            if 0 <= new_i < N and 0 <= new_j < M and not visited[new_i][new_j] and arr[new_i][new_j] > arr[vi][vj]:
                return
            # 델타 중 arr[vi][vj] 랑 같으면 append하고 visited 
            elif 0 <= new_i < N and 0 <= new_j < M and not visited[new_i][new_j] and arr[new_i][new_j] == arr[vi][vj]:
                stack.append((new_i, new_j))
                visited[new_i][new_j] = True
                # 만약 이미 봉우로리 카운트 된 좌표를 만나면 return
                if (new_i, new_j) in cnt_grid:
                    return
            # 델타 중 arr[vi][vj] 보다 작으면 continue    
            elif 0 <= new_i < N and 0 <= new_j < M and not visited[new_i][new_j] and arr[new_i][new_j] < arr[vi][vj]:
                continue
    # while 문이 다 돌면 봉우리 수 cnt + 1
    cnt += 1
    # 시작 좌표 cnt_grid 리스트에 append
    cnt_grid.append((s_i, s_j))

    return



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
cnt_grid = []
for i in range(N):
    for j in range(M):
        visited = [[False] * M for _ in range(N)]
        dfs(i, j)

print(cnt)