N = int(input())
cnt = 0

for _ in range(N):
    word = input()
    check = set()
    
    for i in range(len(word)):
        if i > 0 and word[i] == word[i-1]:
            continue
        if word[i] in check:
            break
        check.add(word[i])
    else:
        cnt +=1
print(cnt)