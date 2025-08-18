T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    W = list(map(int,input().split())) # N개 컨테이너 당 화물 무게
    TM = list(map(int,input().split())) # M개 트럭 적재 용량 트럭 한대당 한개의 컨테이너를 옮길 수 있음
    W.sort(reverse=True)
    TM.sort(reverse=True) # 둘 다 큰 순서대로 정렬

    max_sum = 0
    while len(W)>0 and len(TM)>0:
        # 큰 순서대로 정렬했으므로 W[0]이 TM[0]에 들어가지 않으면 뒤에는 들어갈 수 없음
        if W[0] <= TM[0]:
            max_sum += W[0]
            W.pop(0)
            TM.pop(0)
        elif W[0]>TM[0]:
            W.pop(0)
    print(f"#{tc} {max_sum}")