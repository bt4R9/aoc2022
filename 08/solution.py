raw = open('input', 'r').read().split("\n")
grid = [[int(x) for x in list(line.strip())] for line in raw]
H, W = len(grid), len(grid[0])
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

ans = 0

for y in range(H):
  for x in range(W):
    for dy, dx in dirs:
      ny, nx = y + dy, x + dx
      visible = True
      while 0 <= ny < H and 0 <= nx < W:
        if grid[ny][nx] >= grid[y][x]:
          visible = False
          break

        ny += dy
        nx += dx

      if visible:
        ans += 1
        break

# part 1
print(ans)

ans = []

for y in range(H):
  for x in range(W):
    res = 1
    for dy, dx in dirs:
      line, ny, nx = 0, y + dy, x + dx
      while 0 <= ny < H and 0 <= nx < W:
        line += 1
        if grid[ny][nx] >= grid[y][x]:
          break

        ny += dy
        nx += dx

      res *= line

    ans.append(res)

# part 2
print(max(ans))