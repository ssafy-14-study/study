N = int(input())
nums = [int(input()) for _ in range(N)]

#카운팅정렬(임시리스트 포함)
temp_lst =[0]*N
count_lst = [0]*(max(nums)+1)
for num in nums:
    count_lst[num] += 1

#누적합계산
for i in range(1, len(count_lst)):
    count_lst[i]+=count_lst[i-1]

#정렬된 위치에 배치(원본배열을 뒤에서 부터 순회)
for j in range(N-1,-1,-1):
    n = nums[j]
    #누적합에서 위치 찾기
    p = count_lst[n]-1
    temp_lst[p] = n
    count_lst[n] -= 1

for k in temp_lst:
    print(k)

#버블정렬 (핵심: 비교와 교환)
'''
for i in range(N):
    for j in range(0, N-i-1):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]

for num in nums:
    print(num)

'''

#선택정렬 (핵심: 선택과 배치)
'''
for i in range(N):
    min_idx= i
    for j in range(i+1,N):
        if nums[j] < nums[min_idx]:
            min_idx = j
    
    nums[i],nums[min_idx] = nums[min_idx],nums[i]

for num in nums:
    print(num)
'''
#카운팅정렬기본 (핵심: 개수세기와 누적합)
'''
# 카운팅 배열 만들기
count_lst = [0]*(max(nums)+1)

#개수세기
for i in nums:
    count_lst[i] += 1

for j in range(len(count_lst)):
    for _ in range(count_lst[j]):# 인덱스의 값만큼 반복실행
        print(j)
'''






