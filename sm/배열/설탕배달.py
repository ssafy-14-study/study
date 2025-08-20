# N을 5로 나눈 나머지가
# 1일때 : 몫 -1하고 -> 3*2
# 2일때 : 몫 -2하고 -> 3*4
# 3일때 : 3*1
# 4일때 : 몫 -1하고 -> 3*3
# 단 몫을 뺄수 없는경우 -1 출력

N = int(input())

# 먼저 5kg 봉지를 최대한 사용
five = N // 5
result = -1

while five >= 0:
    remain = N - (five * 5)
    if remain % 3 == 0:   # 나머지를 3kg 봉지로 채울 수 있음
        three = remain // 3
        result = five + three
        break
    five -= 1   # 5kg 봉지 하나 줄이고 다시 시도

print(result)