def switch(Ai, Bi): # switch 함수 정의
    cnt = 0 # 스위치 조작 횟수
    turn = 'on' # 상태 초기값
    for i in range(N):
        if turn == 'on': # 상태가 on이면
            if Ai[i] != Bi[i]: # 전구의 상태가 다를 때 작동
                cnt += 1
                turn = 'off' # 상태를 off로 변경
        if turn == 'off': # 상태가 off면
            if Ai[i] == Bi[i]: # 전구의 상태가 같을 때 작동
                cnt += 1
                turn = 'on' # 상태를 on으로 변경
    return cnt
 
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
    result = switch(Ai, Bi)
 
    print(f'#{test_case} {result}')