T = int(input())

for case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split()))for _ in range(N)]

    #괴물의 좌표 구하기
    x, y = 0,0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x,y = i,j


    #레이저 인덱스 구하기
    lazer_xy = [[x,y]] #벽에 막히지 않는 레이저 좌표 리스트, 괴물 자신은 기본값
    for di,dj in [[1,0],[-1,0],[0,-1],[0,1]]:
        for c in range(1,N):
            ni, nj = x+di*c, y+dj*c
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 1: #벽을 만나면 다른 방향으로
                    break
                lazer_xy.append([ni,nj]) #만나지 않았다면 리스트에 좌표 추가

    #안전한 좌표 갯수 구하기
    safe_cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 and [i,j] not in lazer_xy:
                safe_cnt +=1

    print(f"#{case} {safe_cnt}")