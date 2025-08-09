import sys

N = int(sys.stdin.readline())
lst = [sys.stdin.readline().strip() for _ in range(N)]#개행문자 제거 (중요!! 맨날빼먹음)

set_lst=list(set(lst)) #중복제거
set_lst.sort() # 알파벳순 정렬
set_lst.sort(key=len) #길이순 정렬

for i in set_lst:
    print(i)

# 연습용 내장함수 안쓰고 선택정렬로짠코드 (시간초과)  
# len은 생략하기 어려웠음
'''
set_lst = []
for i in lst:
    if i not in set_lst:
        set_lst.append(i) 
        
#선택정렬
copy_lst =set_lst[:]
sort_lst=[]
while copy_lst:#카피리스트가 없다면 멈춤
    min_num = copy_lst[0]

    for j in copy_lst:
        if len(min_num)>len(j):
            min_num = j

        elif len(min_num) == len(j):
            if min_num > j:
                min_num = j
    
    sort_lst.append(min_num)
    copy_lst.remove(min_num)#반복문을 위해 제거

for i in sort_lst:
print(i)

'''