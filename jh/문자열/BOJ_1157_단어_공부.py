word = str(input())
re_word = word.upper() # 입력받은 word를 전부 대문자로
word_dict = {}
for i in re_word:
    if i not in word_dict:
        word_dict.setdefault(i, 1) # re_word의 알파벳이 word_dict 키에 없다면 생성
    else:
        word_dict[i] += 1# re_word의 알파벳이 word_dict 키에 있다면 값 + 1

max_v = 0
for i in word_dict.values():
    if max_v < i:
        max_v = i # value 값 중 최대 값 찾기

cnt = 0
for i in word_dict.values():
    if max_v == i:
        cnt += 1 # 최대 값의 갯수 찾기

if cnt == 1:
    for k, v in word_dict.items():
        if v == max_v:
            print(f'{k}') # 최대 값이 유일하다면 해당 값을 갖는 키 출력
if cnt >= 2:
    print('?') # 최대 값이 2개 이상이라면 ? 출력