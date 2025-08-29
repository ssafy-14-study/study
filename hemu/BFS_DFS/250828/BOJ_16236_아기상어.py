from collections import deque

N = int(input())

sea = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            sti = i
            stj = j
            sea[i][j]=0
            break

baby_eat = 0
baby_shark = 2
time =0

def find_fish(sea,sti,stj):
    visited = [[0]*N for _ in range(N)]
    visited[sti][stj] = 1
    fish = []
    queue = deque([[sti, stj, 0]])
    while queue:
        a,b,distance = queue.popleft()
  
        for dx,dy in [[-1,0],[0,-1],[1,0],[0,1]]:
            nx,ny = a+dx, b+dy
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:

                if 0<=sea[nx][ny] <=baby_shark:
                    visited[nx][ny] = distance + 1
                    new_distance = distance+1
                    queue.append([nx,ny,new_distance])
                    if 0<sea[nx][ny]<baby_shark:
                        fish.append([nx, ny, new_distance])

    return fish

while True:
    fish_list = find_fish(sea,sti,stj)
    fish_list.sort(key=lambda x:( x[2],x[0],x[1]))
    if len(fish_list)==0:
        break
    a,b,distance = fish_list[0]
    baby_eat +=1
    sea[a][b] = 0
    if baby_eat == baby_shark:
        baby_shark+=1
        baby_eat=0
    time+= distance
    sti = a
    stj = b

print(time)