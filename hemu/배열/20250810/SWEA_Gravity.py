T = int(input())
for tc in range(1,T+1):
    N = int(input())
    C = list(map(int, input().split()))
    max_height = 0   
    for j in C:
        count = 0
        for z in C:
            # 낙차는 결국 N-(나보다 작은것) == 내가 다른것들보다 클때 카운트
            if j>z:
                count += 1
        if count > max_height:
            max_height = count
    print(f"#{tc} {max_height}")