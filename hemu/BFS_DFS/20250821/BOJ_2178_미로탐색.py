from collections import deque
N,M = map(int,input().split())
miro = [list(input()) for _ in range(N)]

# (0,0) -> (N-1,M-1) 1,1 에서 n,m까지로 나와있지만 실제 인덱스는 하나씩 작아야한다.
def bfs(miro,N,M):
    # 시간복잡도 고려
    queue = deque([[0,0]])
    visited = [[0]* M for _ in range(N)]
    visited[0][0] = 1
    while queue:
        tx,ty = queue.popleft()
        if tx == N-1 and ty ==M-1:
            return visited[tx][ty]
        for dx,dy in [[0,1],[1,0],[-1,0],[0,-1]]:
            x,y = tx+dx, ty+dy
            if 0<=x<N and 0<=y<M and miro[x][y]=='1' and visited[x][y] ==0:
                queue.append([x,y])
                visited[x][y] = visited[tx][ty]+1
    return 0

ans = bfs(miro,N,M)
print(ans)