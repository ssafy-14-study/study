T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    Aij = [list(map(int,input().split())) for _ in range(N)]
    safety = 0
    for x in range(N):
        for y in range(M):
            count = 0
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]:
                nx,ny = x+dx, y+dy
                if 0<=nx<N and 0<=ny<M:
                    if Aij[x][y] > Aij[nx][ny]:
                        count += 1
            if count>=4:
                safety += 1
    print(f"#{tc} {safety}")