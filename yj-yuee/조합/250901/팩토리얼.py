N = int(input())

def facto(n): #재귀로 풀기
    if n <= 1:
        return 1 #1반환 후 계산 시작

    return n * facto(n-1)

print(facto(N))