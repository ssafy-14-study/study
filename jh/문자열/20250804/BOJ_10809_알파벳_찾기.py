S = str(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha_list = []
for i in alpha:
    alpha_list.append(i)

for i in alpha_list:
    index_alpha = alpha_list.index(i)
    for j in S:
        index_S = S.index(j)
        if i == j:
            alpha_list[index_alpha] = index_S
            break
        else:
            alpha_list[index_alpha] = -1

for i in alpha_list:
    print(f'{i} ', end = '') 