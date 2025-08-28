def bfs(si, sj, size, eat):
    global travel

    Q = []
    visited = [[-1] * N for _ in range(N)]
    Q.append([si, sj])
    visited[si][sj] = 0
    arr[si][sj] = 0

    # 갈 수 있는 좌표 확인
    while Q:
        [vi, vj] = Q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            new_i = vi + di
            new_j = vj + dj
            if 0 <= new_i < N and 0 <= new_j < N and visited[new_i][new_j] == -1 and arr[new_i][new_j] <= size:
                Q.append([new_i, new_j])
                visited[new_i][new_j] = visited[vi][vj] + 1

    # 먹을 수 있는 물코기 좌표 확인 및 거리 추가
    can_eat = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] < size and arr[i][j] != 0:
                can_eat.append([i, j])
    distance = []
    for i in can_eat:
        if visited[i[0]][i[1]] > 0:
            distance.append([visited[i[0]][i[1]], i[0], i[1]])
    distance.sort()

    # 먹을 수 있는 물코기가 있을 동안 동작
    while distance:

        # 상어 크기와 먹은 물코기 수가 같지 않을 때
        if size != eat:
            a = distance.pop(0)
            travel += a[0]
            eat += 1
            [si, sj] = [a[1], a[2]]
            arr[a[1]][a[2]] = 0
            if size == eat:
                size += 1
                eat = 0
            return bfs(si, sj, size, eat)
    else:
        return travel

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
size = 2 # 상어 크기
eat = 0 # 먹은 물코기 수
travel = 0 # 상어 총 이동 거리

# 시작 위치 구하기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            [si, sj] = [i, j]
result = bfs(si, sj, size, eat)

print(result)