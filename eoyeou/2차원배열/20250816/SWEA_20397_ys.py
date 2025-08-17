'''
돌의 양면 흰색, 검은색
i번째 돌 사이에 두고 마주보는 j개의 돌 
각각 같은 색이면 뒤집고, 다른 색이면 그대로 둔다..
범위 벗어나면 중지
'''
def switch_stone(i):              # 1->0 , 0->1 바꾸는 함수
    if stones[i] == 1:
        stones[i] = 0
    elif stones[i] == 0:
        stones[i] = 1
 
 
T = int(input())
for casenum in range(1, T+1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
 
        for k in range(1,j+1):                  #1~j번 반복
            if (i-1-k) < 0 or (i-1-k) >=N or (i-1+k) <0 or (i-1+k) >= N:        #인덱스 범위 설정
                break
            elif stones[i-1-k] != stones[i-1+k]:                        # i기준으로 다르면 건너뛰고 
                continue
            elif stones[i-1-k] == stones[i-1+k]:                        # 같으면 0->1, 1 ->0바꿔주기
                switch_stone(i-1-k)
                switch_stone(i-1+k)
 
  
         
 
    print(f"#{casenum} {' '.join(map(str, stones))}")  