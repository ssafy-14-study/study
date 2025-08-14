T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if M[i][j] == 2:
                mon_i, mon_j = [i, j] # 괴물 위치 인덱스 저장

    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]: # 괴물 위치 기준 상하좌우 탐색
        for k in range(N):
            new_i = mon_i + di * k
            new_j = mon_j + dj * k
            if 0 <= new_i < N and 0 <= new_j < N:
                if M[new_i][new_j] == 0: # 빈칸이면
                    M[new_i][new_j] = 1 # 1로 변경
                elif M[new_i][new_j] == 1: # 벽이면 그 방향 탐색 종료
                    break
    cnt = 0
    for i in range(N):
        for j in range(N):
            if M[i][j] == 0:
                cnt += 1 # 안전한 빈 칸 수 카운트

    print(f'#{test_case} {cnt}')