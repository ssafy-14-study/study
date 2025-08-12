N = [list(map(int, input().split())) for _ in range(9)]
max_v = 0
idx_row = 0
idx_col = 0
cur_row = 0
for i in N[:]:
    if max_v < max(i):
        max_v = max(i)
        idx_row = cur_row
        idx_col = i.index(max(i))
    cur_row += 1

print(max_v)
print(idx_row + 1, idx_col + 1)