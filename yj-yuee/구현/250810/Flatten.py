for ts in range(10):#평탄화하기
    def max_box(lst): # 리스트에서 가장큰값 찾기
        max_ = lst[0]
        max_idx = 0
        for i in range(len(lst)):
            if max_ < lst[i]:
                max_ = lst[i]
                max_idx = i
        boxes[max_idx] -= 1 #가장큰값 -1
        return max_
    def min_box(lst):# 가장 작은값 찾기
        min_ = lst[0]
        min_idx = 0
        for i in range(len(lst)):
            if min_ > lst[i]:
                min_ = lst[i]
                min_idx = i
        boxes[min_idx] += 1 #가장 작은값 +1
        return min_

    N = int(input())
    boxes = list(map(int,input().split()))
    for i in range(N):
        a = max_box(boxes)
        b = min_box(boxes)
        if a - b <= 1: #차이가 1이거나 0이면 탈출
            break
    final_max = boxes[0] #최종리스트 max, min찾기
    final_min = boxes[0]
    for j in boxes:
        if final_max < j :
            final_max = j
        if final_min > j:
            final_min = j
    print(f'#{ts+1} {final_max - final_min}')