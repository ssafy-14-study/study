# 논리적으로 동일 제출결과 fail
# word = input()
# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=','z=']

# count = 0
# for i in croatia:
#     if i in word: ## 불필요한 조건으로 메모리 낭비가능성?
#         count += word.count(i)
#         word = word.replace(i,'')
# count += len(word)
# print(count)

#count보다 메모리낭비 x 틀린이유가 시간초과가 아니라 의아하지만 더 효율적인 코드!
word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=','z=']

for i in croatia:
    word = word.replace(i, '*')

print(len(word))