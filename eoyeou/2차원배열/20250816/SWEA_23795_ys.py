def direction(dr, dc):
    for k in range(1, N):                               #델타 이용 함수
        new_r = dr * k + row
        new_c = dc * k + col
        if 0 <= new_r < N and 0 <= new_c < N:
            if board[new_r][new_c] == 1:            # 벽을 만나면 종료
                return
 
            if board[new_r][new_c] == 0:        
                board[new_r][new_c] = 3             # 0인 곳을 3으로 바꿔주기
 
 
T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
 
    monster = board[0][0] 
    cnt = 0
    for row in range(N):
        for col in range(N):
            if board[row][col] == 2:
                monster = board[row][col]               #괴물 위치 설정
 
 
                direction(1, 0)                         # 상하좌우 실행
                direction(0, 1)
                direction(-1, 0)
                direction(0, -1)
 
                 
    for row in range(N):
        for col in range(N):      
            if board[row][col] == 0:                    #보드 전체를 돌면서 0인 곳 count 
                cnt +=1
    print(f'#{case_num} {cnt}')