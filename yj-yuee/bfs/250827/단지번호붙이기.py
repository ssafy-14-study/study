from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
#연결된 집을 찾아서 단지수를 출력하고 단지에 속하는 집의 수

def bfs(ni, nj):
    global cnt
    visited[ni][nj] = True
    Q.append([ni,nj]) # 큐에 값 추가
    while Q:
        vi,vj = Q.popleft()
        for k in range(4):
            wi = vi + dx[k]
            wj = vj + dy[k]
            if 0<= wi < N and 0<= wj <N and graph[wi][wj] == '1' and visited[wi][wj] != True:
                cnt += 1
                visited[wi][wj] = True
                Q.append([wi,wj])

N = int(input())
graph = [input() for _ in range(N)]

danji = []
visited = [[False] * N for _ in range(N)]

Q = deque()
# 시작점을 모르는데 흠
for i in range(N):
    for j in range(N):
        if graph[i][j] == '1' and visited[i][j] == False:
            cnt = 1
            bfs(i,j)
            danji.append(cnt)

danji.sort()
print(len(danji))
for l in danji:
    print(l)

#문자열이라 오류가남 lsit로 묶던가 visited만들던가