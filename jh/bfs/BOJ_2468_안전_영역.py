def safe_area(height): # 물의 높이를 dfs 함수의 인풋으로 설정
    safe = [[0] * N for _ in range(N)] # 0으로 이루어진 2차원 배열 생성
    for i in range(N): # 물의 높이보다 높은 좌표들은 값을 1로 변경
        for j in range(N):
            if arr[i][j] > height:
                safe[i][j] = 1
    start_point = [] # 안전 영역들을 시작 지점으로 설정
    for i in range(N):
        for j in range(N):
            if safe[i][j] == 1:
                start_point.append([i, j])
    cnt = 0 # 여기서부터 실질적인 bfs 코드
    for i in start_point: 
        if safe[i[0]][i[1]] == 1:
            stack = []
            cnt += 1
            stack.append(i)
            safe[i[0]][i[1]] = 0
            while stack:
                [vi, vj] = stack.pop()
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    new_i = vi + di
                    new_j = vj + dj
                    if 0 <= new_i < N and 0 <= new_j < N and safe[new_i][new_j] == 1:
                        stack.append([new_i, new_j])
                        safe[new_i][new_j] = 0
    return cnt

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_v = 0
for i in range(N): # 배열에서 최대 값 찾기
    for j in range(N):
        if max_v < arr[i][j]:
            max_v = arr[i][j]
result = 0
for i in range(max_v + 1): # 물의 높이에 따른 안전 영역 구하기
    cnt_cur = safe_area(i)
    if result < cnt_cur:
        result = cnt_cur

print(result)