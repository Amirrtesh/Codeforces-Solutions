matrix = []
for _ in range(5):
  row = list(map(int, input().split()))
  matrix.append(row)
 
row_one = -1
col_one = -1
 
for r in range(5):
  for c in range(5):
    if matrix[r][c] == 1:
      row_one = r
      col_one = c
      break
  if row_one != -1:
    break
moves = abs(row_one - 2) + abs(col_one - 2)
print(moves)
