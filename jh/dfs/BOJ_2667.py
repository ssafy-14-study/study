def dfs():
    global danji_num
    stack = []
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '1': # arr를 순환하다가 집 발견
                danji_num += 1 # 단지의 수 + 1
                danji_cnt = 1 # 단지 내 집의 수 + 1
                stack.append([i, j])
                arr[i][j] = '0'
                visited[i][j] = True
                while stack:
                    [vi, vj] = stack.pop()
                    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        new_i = vi + di
                        new_j = vj + dj
                        if 0 <= new_i < N and 0 <= new_j < N and arr[new_i][new_j] == '1' and visited[new_i][new_j] == False:
                            stack.append([new_i, new_j])
                            arr[new_i][new_j] = '0'
                            visited[new_i][new_j] = True
                            danji_cnt += 1 # 단지 내 집의 수 + 1
                danji.append(danji_cnt)
    return()

N = int(input())
arr = list(list(input()) for _ in range(N))
danji = [] # 단지 내 집의 수 담을 리스트
danji_num = 0 # 단지의 수
dfs()
danji.sort()
print(danji_num)
for i in danji:
    print(i)