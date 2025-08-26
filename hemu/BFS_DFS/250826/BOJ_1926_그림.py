from collections import deque
n,m = map(int,input().split())
art = [list(map(int,input().split())) for _ in range(n)]


def bfs(art,i,j):
    count =1
    art[i][j]=2
    queue = deque([[i,j]])
    while queue:
        x,y = queue.popleft()
        for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx,ny = dx+x,dy+y

            if 0<=nx<n and 0<=ny<m and art[nx][ny]==1:
                count += 1
                art[nx][ny] =2
                queue.append([nx,ny])
    return count



# bfs로 가는 길을 2로 바꿔주기 때문에 1을 찾으면 그게 그림의 개수
total =0
max_count = 0
for i in range(n):
    for j in range(m):
        if art[i][j] ==1:
            total +=1
            a = bfs(art,i,j)
            if a>max_count:
                max_count =a
print(total)
print(max_count)