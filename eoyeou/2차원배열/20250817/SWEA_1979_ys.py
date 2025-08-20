'''
1인 곳 찾아서 -> 시작이 1이어야( 시작 전은 0이거나 없거나)
k만큼 세기
cnt == k ->place += 1 

중복값 빼기 K=3일때
11100 -> ok
11110 -> Not OK
'''


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    place = 0
    for row in range(N):
        for col in range(N):
            if puzzle[row][col] == 1:               #1인 지점을 찾아서
                cnt = 0
                if (row == 0 or puzzle[row-1][col] == 0) and (row+K>=N or puzzle[row+K][col] == 0): #시작 전과 끝 다음 값이 0이어야 
                    for i in range(row, row+K):
                        if 0 <= i < N:
                            if puzzle[i][col] != 1:
                                break
                            else: cnt +=1               #연속으로 1일때만 카운트
                    if cnt == K:
                        place += 1

                cnt = 0
                if (col == 0 or puzzle[row][col-1] == 0) and (col+K>=N or puzzle[row][col+K] == 0):
                    for j in range(col, col+K):
                        if 0<=j < N :
                            if puzzle[row][j] != 1:
                                break
                            else: cnt +=1
                    if cnt == K:
                        place += 1

    print(f'#{t} {place}')