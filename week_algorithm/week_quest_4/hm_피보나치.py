T = int(input())
for tc in range(T):
    zero_count =[1,0]
    one_count = [0,1]
    a = int(input())
    if a>1:
        for i in range(2,a+1):
            if len(zero_count)<=i and len(one_count)<=i:
                zero_count.append(zero_count[i-1]+zero_count[i-2])
                one_count.append(one_count[i-1]+one_count[i-2])
    
    print(zero_count[a],one_count[a])