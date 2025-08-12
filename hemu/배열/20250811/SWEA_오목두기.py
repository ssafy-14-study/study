T = int(input())
for tc in range(1,T+1):
    N = int(input())
    omok = [list(input()) for _ in range(N)]
    
    def check_omok(omok,N):
        # 상하좌우, 대각선 방향 필요
        direction = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
        for i in range(N):
            for j in range(N):
                if omok[i][j] == 'o':
                    for di, dj in direction:
                        count = 1
                        # z의 범위 넉넉하게 잡기, 자기자신은 포함 하지 않아야 하므로 1부터 시작
                        for z in range(1,N):
                            ni,nj = i +di*z, j+dj*z
                            # 인덱스 에러 나지 않게 범위 조정
                            if 0<=ni<N and 0<=nj<N and omok[ni][nj] == 'o':
                                count += 1
                            else:
                                break
                        if count >= 5:
                            return True
        return False
    
    
    if check_omok(omok,N):
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")