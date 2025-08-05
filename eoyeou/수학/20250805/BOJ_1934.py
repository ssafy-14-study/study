def gcd(a,b): 
    if (b == 0): 
        return a
    else:
        return gcd(b, a%b)
    
T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    c = gcd(A,B)
    print((A * B) //c)