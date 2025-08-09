N = int(input())
arr = [[0] * 100 for _ in range(100)] #도화지 만들기

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = 1  # 1은 색종이가 올라갔음을 뜻함

# 넓이 계산
area = 0
for row in arr:
    area += sum(row)

print(area)