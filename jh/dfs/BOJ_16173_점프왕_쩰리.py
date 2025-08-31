def bfs(si, sj):
    stack = []
    stack.append([si, sj]) # 처음 시작 인덱스 stack에 append
    visited = [[False] * N for _ in range(N)]
    visited[si][sj] = True # 처음 시작 인덱스 True로 변경
    while stack:
        vi, vj = stack.pop()
        for di, dj in [[0, 1], [1, 0]]: # 오른쪽, 아래쪽 으로만 진행
            new_i = vi + di * arr[vi][vj] # 해당 좌표의 값만큼 곱한 만큼 진행
            new_j = vj + dj * arr[vi][vj]
            if 0 <= new_i < N and 0 <= new_j < N and visited[new_i][new_j] == False:
                stack.append([new_i, new_j])
                visited[new_i][new_j] = True
                if arr[new_i][new_j] == -1: # 목표 좌표에 도달하면 HaruHaru 출력
                    return print('HaruHaru')
    else:
        return print('Hing') # 목표 좌표에 도달하지 못했으면 Hing 출력

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
si, sj = 0, 0
bfs(si, sj)