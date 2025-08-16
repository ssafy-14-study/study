def dfs(miro,x,y,N):
    if x <0 or x>= N or y<0 or y>= N:
        return False
    if miro[x][y] =='3':
        return True
    if miro[x][y] == '1' or miro[x][y] == '-1':
        return False

    
    miro[x][y] = '-1'
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx,ny = x+dx,y+dy
        if dfs(miro,nx,ny,N):
            return True
    return False


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    miro = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if miro[i][j] == '2':
                S_x = i
                S_y = j
    result = dfs(miro,S_x,S_y,N)
    if result:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
