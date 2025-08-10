word = list(input() for _ in range(5))

max_l = 0
for _ in word:
    l= len(_)
    if max_l < l :
        max_l = l

for i in range(max_l):
    for j in range(5):
        if i < len(word[j]):
            print(word[j][i], end='')   