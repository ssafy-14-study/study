N = int(input())
Pi = list(map(int,input().split()))


def get_total_time(Pi_list,N):
    time_sum = 0
    # 앞에서부터 하나씩 더한 값을 리스트에 다시 저장
    for i in range(N):
        time_sum += Pi_list[i]
        Pi_list[i] = time_sum
    total_time = 0
    # 새로 만든 리스트의 요소들의 합
    for j in Pi_list:
        total_time += j
    return total_time


# 결국 작은 순서대로 정리했을때가 최솟값
a =sorted(Pi)
result = get_total_time(a,N)
print(result)