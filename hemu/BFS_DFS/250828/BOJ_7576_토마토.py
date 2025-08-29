from collections import deque

M,N = map(int,input().split())

tomato = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

start_list =deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            
            start_list.append([i,j,0])

def bfs(start_list,tomato):
    # 반드시 익은 토마토가 있다는 보장이 없으므로 안에서 정의해야함
    day=0
    while start_list:
        sti,stj,day = start_list.popleft()
        for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx,ny = dx+sti,dy+stj
            if 0<=nx<N and 0<=ny<M:
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] =1
                    new_day = day+1
                    start_list.append([nx,ny,new_day])
    return day

new_tomato = bfs(start_list,tomato)
for a in range(N):
    for b in range(M):
        if tomato[a][b] ==0:
            new_tomato=-1
            break
print(new_tomato)