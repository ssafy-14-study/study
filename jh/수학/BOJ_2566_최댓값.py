N = [list(map(int, input().split())) for _ in range(9)]
max_v = 0
idx_row = 0
idx_col = 0
cur_row = 0
for i in N[:]:
    if max_v < max(i):
        max_v = max(i)
        idx_row = cur_row # 행의 인덱스를 카운트
        idx_col = i.index(max(i)) # 열의 인덱스
    cur_row += 1

print(max_v)
print(idx_row + 1, idx_col + 1) # 문제에서 요구하는 행과 열은 1행 1열부터 시작