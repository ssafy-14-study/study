num_list = []
while(1):
    a, b = map(int,(input().split()))
    if (a == 0 and b == 0):
        break
    num_list.append((a,b))
        
for a, b in num_list :
    if a == 0 or b == 0 :
        print('neither')
    elif b % a == 0 :
        print('factor')
    elif a % b == 0 :
        print('multiple')
    else : print('neither')