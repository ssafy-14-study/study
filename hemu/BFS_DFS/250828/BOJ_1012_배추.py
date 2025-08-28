from collections import deque

T = int(input())
for tc in range(1,T+1):
    M,N,K = map(int,input().split())
    bat = [[0]*M for _ in range(N)]

    

    for _ in range(K):
        a,b = map(int,input().split())
        bat[b][a] = 1
     


    def bfs(i,j,bat):
        bat[i][j] = 2
        queue = deque([[i,j]])
        while queue:
            x,y =queue.popleft()
            for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                nx,ny =dx+x,dy+y
                if 0<=nx<N and 0<=ny<M and bat[nx][ny]==1:
                    bat[nx][ny] =2
                    queue.append([nx,ny])

    count = 0
    for i in range(N):
        for j in range(M):
            if bat[i][j] == 1:
                bfs(i,j,bat)
                count += 1

    print(count)

