T = int(input())
for tc in range(1,T+1):
    N = int(input())
    pung = [list(map(int, input().split())) for _ in range(N)]
    max_pung = 0
    for x in range(N):
        for y in range(N):
            s = pung[x][y]
            num = [[1,0],[-1,0],[0,1],[0,-1]]
            for dx, dy in num:
                for z in range(1,N):
                    nx, ny = x+dx*z, y+dy*z
                    if 0<=nx<N and 0<=ny<N:
                        s+=pung[nx][ny]
                if s>max_pung:
                    max_pung = s
    print(f"#{tc} {max_pung}")
