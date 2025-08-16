T = int(input())
for test in range(1, T+1):
    N = int(input())
    switch = list(map(int, input().split()))
    ctrl_switch = list(map(int, input().split()))
 
    cnt = 0
    while(switch != ctrl_switch):                   # 스우치 조작 후 리스트와 같아질 때까지 반복
        if switch == ctrl_switch:                   # 같아지면 종료
            break
        for i in range(len(switch)):                # 스위치 리스트를 돌면서                
            if switch[i] == ctrl_switch[i]:         # switch 조작 전 == 조작 후
                continue                            # 건너뛰기
            elif switch[i] != ctrl_switch[i]:       # 스위치 조작 전 != 조작 후       
                idx = i                             # 인덱스를 변수 idx에 저장
                cnt += 1                            # 카운트 증가
                break                               
        for j in range(idx,len(switch)):            # idx부터 끝까지 
            if switch[j] == 0:                      # 0 -> 1 , 1->0    
                switch[j] = 1
            elif switch[j] == 1:
                switch[j] = 0
 
 
    print(f'#{test} {cnt}')