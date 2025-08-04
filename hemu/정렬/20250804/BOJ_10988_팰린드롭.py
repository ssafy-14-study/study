N = list(input())
sort_n = N[::-1]
count = 0
for i in range(len(N)):
    if N[i] != sort_n[i]:
        count += 1
if count == 0:
    print(1)
else:
    print(0)