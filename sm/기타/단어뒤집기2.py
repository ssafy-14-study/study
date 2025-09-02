# 태그 : < >, 길이 3이상인 문자열 안에는 알파벳소문자와 공백만 존재
# 단어 : 알파벳소문자와 숫자로 이루어진 문자열
# 연속하는 두 단어는 공백으로 구분

# 태그x, 단어만 뒤집는다.

string = input()

rever = 0
ans = []
lst = ''

 
for i in string:
    if i == '<':
        rever = 1
    elif i == '>':
        rever = 0
        ans.append(lst+'>')
        lst = ''
        continue
        

    if rever == 1:
        lst = lst + i
        
    if rever == 0:
        if i == ' ':
            lst = lst + ' '
            ans.append(lst)
            lst = ''
        else:
            lst = i + lst
ans.append(lst)
lst = ''
print(f'{"".join(ans)}')

            
            



# i=0
# while i< len(string):
#     if string[i] == '<':
#         while string[i] != '>':
#             print(i, end='')
#             i += 1
#         print(">", end='')
#         i += 2
#     else:
#         print('a')
#         i+=1