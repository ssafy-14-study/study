N = int(input())
words = []
for i in range(N):
    word = list(map(str, input()))
    words.append(word) # 입력받은 문자들을 리스트에 저장

cnt = 0
for i in words:
    idx = 0
    while idx < len(i) - 1: # 처음에는 for문을 사용했지만 문자가 pop 되면 i의 길이가 달라지기 때문에 while문으로 교체
        if i[idx] == i[idx + 1]: # 현재 인덱스의 문자와 다음 인덱스의 문자를 비교
            i.pop(idx) # 같으면 현재 인덱스의 문자를 제거
        else:
            idx += 1 # 같지 않으면 idx + 1
    if len(i) == len(set(i)): # 연속된 문자를 제거한 i와 중복을 모두 제거하는 set(i)와 비교
        cnt += 1

print(cnt) 