#난쟁이가 갑자기 9명 - 백설공주가 기억하는 7난쟁이 키의 합 100
#9난쟁이 키가 주어졌을때 일곱난쟁이를 찾아라
dwarfs = [int(input()) for _ in range(9)]

#완전 탐색
total_dwarfs = sum(dwarfs)
for i in range(9):
    for j in range(i+1,9):
        if total_dwarfs - dwarfs[i]-dwarfs[j] == 100: #두개를 뺐을때 100이 될때까지 탐색
            fake1, fake2 = dwarfs[i], dwarfs[j]
            break


dwarfs_7 = [k for k in dwarfs if k != fake1 and k != fake2]
dwarfs_7.sort()#정렬후 출력

for j in dwarfs_7:
    print(j)