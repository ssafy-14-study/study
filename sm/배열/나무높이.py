T = int(input())
for case in range(1,T+1):
    N = int(input())
    height = list(map(int,input().split()))

    max_height = max(height) # 키가 가장 큰 나무

    sum_diff = 0                     # 총 자라야할 나무의 높이를 구할 변수
    odd = 0                         # 자라야할 나무의 높이가 홀수인 경우
    for tree in height:
        diff = max_height - tree       # diff == 각 나무의 자라야할 높이
        sum_diff += diff                
        if diff % 2:                    # diff가 홀수이면, odd += 1
            odd += 1

    days = (sum_diff // 3) * 2 + (sum_diff % 3)   # sum_diff에 대해 가장 이상적인 최단기간
    one = days // 2 + days % 2                  # 최단기간에서의 홀수날짜
    two = days // 2                             # 최단기간에서의 짝수날짜

    if odd <= one:                  # 필요한 높이가 홀수인 경우의 수가 , 최단기간에서의 홀수날짜보다 적으면 최단기간으로 해결 가능
        result = days               
    else:                           # 필요한 높이가 홀수인 경우의 수가 , 최단기간에서의 홀수날짜보다 크다면 부족한 홀수날짜가 나올때까지 기다려야하므로 총 홀수의 날짜
        result = 2 * odd - 1        

    print(f'#{case} {result}')