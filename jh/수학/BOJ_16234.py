def dfs(s_i, s_j):
    global is_moved
    # stack 사용
    stack = []
    stack.append((s_i, s_j))
    visited[s_i][s_j] = True
    # 국경이 연결된 지역의 인구수, 나라 수, 좌표 리스트를 활용
    tmp_sum = arr[s_i][s_j]
    tmp_cnt = 1
    tmp_list = []
    tmp_list.append((s_i, s_j))
    while stack:
        vi, vj = stack.pop()
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_i = vi + di
            new_j = vj + dj
            if 0 <= new_i < N and 0 <= new_j < N and not visited[new_i][new_j]:
                tmp_diff = abs(arr[vi][vj] - arr[new_i][new_j])
                if L <= tmp_diff <= R:
                    stack.append((new_i, new_j))
                    visited[new_i][new_j] = True
                    tmp_sum += arr[new_i][new_j]
                    tmp_cnt += 1
                    tmp_list.append((new_i, new_j))
    # 만약 이번 dfs로 True로 변경된 나라의 수가 2개 이상이면
    if tmp_cnt >= 2:
        # arr 업데이트
        after_move = tmp_sum // tmp_cnt
        for i, j in tmp_list:
            arr[i][j] = after_move
        # is_moved True
        is_moved = True

    return visited


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

# 결과
result = 0

while True:
    # 인구 이동이 일어났는지 체크하는 is_moved 초기값 설정
    is_moved = False
    # visited 초기화
    visited = [[False] * N for _ in range(N)]
    # 전체 좌표를 탐색
    for i in range(N):
        for j in range(N):
            # 방문하지 않은 곳의 좌표에 대해 dfs 수행
            if not visited[i][j]:
                visited = dfs(i, j)
    # 모든 좌표 탐색 후 인구 이동이 일어나지 않았으면 break, 인구이동이 일어났으면 result += 1
    if not is_moved:
        break
    else:
        result += 1

print(result)