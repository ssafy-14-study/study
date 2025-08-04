fac_num = int(input())
fac_list = list(map(int, input().split()))
fac_list.sort()

if fac_num % 2 == 0 :
    print(fac_list[0] * fac_list[-1])
else :
    print(fac_list[fac_num//2]**2)