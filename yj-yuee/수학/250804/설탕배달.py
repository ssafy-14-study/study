N  = int(input())

result = -1
for i in range(N // 5, -1 , -1):
    rest = N - (5 * i) 
    if rest % 3 == 0 :
        result = i + (rest // 3)
        break
   
print(result)