from collections import deque

T = int(input())
for tc in range(T):
    N = int(input())
    a,b = map(int,input().split())
    c,d = map(int,input().split())

    chess = [[0]*N for _ in range(N)]

  # 최단거리 구하기
    def bfs(chess,a,b,c,d):
        queue =deque([[a,b]])
        while queue:
            x,y = queue.popleft()
            if x==c and y==d:
                break
            # 나이트가 이동한 방향
            for dx,dy in [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]:
                nx,ny = x+dx,y+dy

                if 0<=nx<N and 0<=ny<N and chess[nx][ny] == 0:
                    chess[nx][ny] = chess[x][y]+1
                    # 나이트가 이동한 횟수
                    queue.append([nx,ny])
        return chess[x][y]

    a = bfs(chess,a,b,c,d)
    print(a)
