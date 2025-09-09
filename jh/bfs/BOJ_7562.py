def bfs(cur):
    Q = []
    visited = [[-1] * l for _ in range(l)] # 체스판 생성
    Q.append(cur)
    visited[cur[0]][cur[1]] = 0 # 처음 시작 좌표의 값은 0
    while Q:
        [vi, vj] = Q.pop(0)
        for di, dj in [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]: # 나이트의 이동 가능한 델타
            new_i = vi + di
            new_j = vj + dj
            if 0 <= new_i < l and 0 <= new_j < l and visited[new_i][new_j] == -1:
                Q.append([new_i, new_j])
                visited[new_i][new_j] = visited[vi][vj] + 1 # 그 전 좌표 값의 + 1
    return visited

T = int(input())
for testcase in range(1, T + 1):
    l = int(input())
    cur = list(map(int, input().split()))
    goal = list(map(int, input().split()))
    result = bfs(cur)

    print(result[goal[0]][goal[1]])