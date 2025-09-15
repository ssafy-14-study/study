import pprint
T= int(input())
for tc in range(1,T+1):
    N,M,R,C,L = map(int,input().split())
    # N:세로크기 M: 가로크기  R: 맨홀 뚜껑 위치한 장소의 세로위치 C: 가로위치 L: 탈출 후 소요 시간
    under = [list(map(int,input().split())) for _ in range(N)]
 
    direction = {1:[[1,0],[0,1],[-1,0],[0,-1]], 2: [[-1,0],[1,0]], 3: [[0,-1],[0,1]], 4:[[-1,0],[0,1]], 5: [[1,0],[0,1]], 6: [[1,0],[0,-1]],7:[[-1,0],[0,-1]]}
 
    visited = [[False]*M for _ in range(N)]
 
 
    def find_thief(R,C,visited):
        stack = [[R,C,1]]
        visited[R][C] = True
         
 
        while stack:
  
            x,y,depth = stack.pop(0)
            if depth ==L:
                break
      
            for dx,dy in direction[under[x][y]]:
      
                nx,ny = x+dx, y+dy
 
                if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False and under[nx][ny]>0:
                    if [dx,dy] == [0,-1]:
                        if under[nx][ny] in [1,3,4,5]:
                            visited[nx][ny] = True
                            stack.append([nx,ny,depth+1])
                    elif [dx,dy] == [0,1]:
                        if under[nx][ny] in [1,3,6,7]:
                            visited[nx][ny] = True
                            stack.append([nx,ny,depth+1])
                    elif [dx,dy] == [-1,0]:
                        if under[nx][ny] in [1,2,5,6]:          
                            visited[nx][ny] = True                          
                            stack.append([nx,ny,depth+1])
                    elif [dx,dy] == [1,0]:
                        if under[nx][ny] in [1,2,4,7]:                                        
                            visited[nx][ny] = True
                            stack.append([nx,ny,depth+1])
 
 
 
        return visited
     
    count =0
    A = find_thief(R,C,visited)
    for i in range(N):
        for j in range(M):
            if A[i][j] == True:
                count +=1
     
 
    print(f"#{tc} {count}")
