T= int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split()) # S의길이 = N, 붕빵 만드는데 M초 시간들이면 K개 만듦
    S = list(map(int,input().split())) # 손님이 언제 도착? 처음에 nmk의 순서를 잘못해 fail이 떴었다.
 
    S.sort()
    give = 0
 
    for j in S:
        bung = (j//M)*K # 손님이 도착할때 붕어빵 개수
        if bung > give :
            give += 1 # 줄때마다 카운트
        else:
            print(f"#{tc} Impossible")
            break     
    else:
        print(f"#{tc} Possible")