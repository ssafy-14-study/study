T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cur_max = 0
    cnt = 0
    for i in range(N): # 가로줄 확인을 위한 for문
        for j in range(M): 
            if arr[i][j] == 1: # 처음 1을 발견하면
                cnt = 1 # cnt 1 증가
                for k in range(1, M - j): # 거기서부터 그 줄의 끝까지 반복
                    if arr[i][j + k] == 1: # 1이 연속으로 나오면
                        cnt += 1 # cnt 증가
                    else:
                        break # 0이 나오면 중지
            if cur_max < cnt: # 한 줄에서 나온 cnt를 전의 max값과 비교
                cur_max = cnt 

    cnt = 0 # cnt 초기화
    for i in range(M): # 세로줄 확인을 위한 for문
        for j in range(N):
            if arr[j][i] == 1: # 위의 for문과 똑같은 동작
                cnt = 1
                for k in range(1, N - j):
                    if arr[j + k][i] == 1:
                        cnt += 1
                    else:
                        break
            if cur_max < cnt:
                cur_max = cnt

    if cur_max == 1: # 전체 가로, 세로줄을 다 돌았는데 max 값이 1이면
        result = 0 # 노이즈로 판별하고 0 반환
    else:
        result = cur_max

    print(f'#{test_case} {result}')