#N개의 스위치
#남학생은 자기가 받은 수의 배수이면 스위치의 상태를 바꾼다.
#여학생은 자기가 받은 수의 스위치를 중심으로 좌우가 대칭미녀서 가장많은 스위치를 포함하는 구간을 찾아 모두바꿈
N = int(input())
switch_lst = list(map(int, input().split()))
S = int(input())
S_list = [list(map(int, input().split())) for _ in range(S)]

for gen, num in S_list:
    if gen == 1: #남학생일때
        for i in range(1,N+1):
            if i % num == 0 : #본인의 배수 라면
                switch_lst[i-1] = 1-switch_lst[i-1]#0 이면 1 ,1 이면 0으로 바꾼다(토글 사용)


    if gen == 2: #여학생일때
        #나는 무조건 바꾼다.
        switch_lst[num-1] = 1-switch_lst[num-1]

        #양옆으로 하나씩 대칭인지 확인
        l_idx = num - 2
        r_idx = num  # 왼쪽 오른쪽
        while l_idx >= 0 and r_idx < N: #범위 안에 있을때만 반복(범위진짜 맨날 어려움)
            if switch_lst[l_idx] == switch_lst[r_idx]: #대칭이라면
                #양쪽다 바꿈
                switch_lst[l_idx] = 1 - switch_lst[l_idx]
                switch_lst[r_idx] = 1 - switch_lst[r_idx]
                l_idx -= 1 # 좌우 인덱스를 증가시켜 계속 탐색한다.
                r_idx += 1
            else:#대칭이 아니면
                break
            #탈출


if N <= 20:
    print(*switch_lst)
else:
    for n in range(0, N, 20):
        print(*switch_lst[n:n+20])

'''# 런타임에러 (처음값, 마지막값 인덱스에러로 추측)
    if gen == 2: #여학생일때
        #내숫자의 대칭이 같다면 나포함 같은 부분까지 상태를 바꾸고(num= index[num -1])
        if switch_lst[num-2] == switch_lst[num]:
            l_idx = num-2
            r_idx = num  # 아래 포문에서 계산하기 위해 변수할당
            while l_idx >= 0 and r_idx < len(switch_lst) and switch_lst[l_idx] == switch_lst[r_idx]: #좌우가 같지않을때 까지
                if switch_lst[l_idx] == 0 and switch_lst[r_idx] == 0:
                    switch_lst[l_idx],switch_lst[r_idx] = 1,1
                else:
                    switch_lst[l_idx], switch_lst[r_idx] = 0,0
                l_idx -= 1 # 좌우 인덱스를 증가시켜 계속 탐색한다.
                r_idx += 1
            #반복문을 탈출하면 나도 바꾼다
            if switch_lst[num - 1] == 0:  # 0 이면 1 ,1 이면 0으로 바꾼다
                switch_lst[num - 1] = 1
            else:
                switch_lst[num - 1] = 0
        else :#내숫자의 양옆 대칭이 다르면 나만 바꾼다
            if switch_lst[num - 1] == 0:  # 0 이면 1 ,1 이면 0으로 바꾼다
                switch_lst[num - 1] = 1
            else:
                switch_lst[num - 1] = 0
'''