T = int(input())
for x in range(1,T+1):
    N, M, K = map(int, input().split())
    N_lst = list(map(int, input().split()))
    N_lst.sort()
    result = 'Possible'
    for i in range(N):
        #손님이 도착했을때 붕어빵이 1이상 있는지
        #손님도착시간 나누기 M초 * K -> t초까지 만들어진 붕어빵 총개수
        t = N_lst[i]
        if (t // M) * K < i + 1:
            result = 'Impossible'
            break

    print(f'#{x} {result}')