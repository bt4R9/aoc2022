from collections import deque

def solve(part):
  grid = [list(row) for row in open('input', 'r').read().split('\n')]
  H, W = len(grid), len(grid[0])
  q = deque()
  end = (-1, -1)

  for y in range(H):
    for x in range(W):
      if grid[y][x] == "S":
        grid[y][x] = "a"
        q.append((y, x, 0))
      if grid[y][x] == "E":
        end = y, x
        grid[y][x] = "z"
      if part == 2 and grid[y][x] == "a":
        q.append((y, x, 0))

  vis = set()

  while q:
    y, x, c = q.popleft()

    if (y, x) == end:
      return c

    if (y, x) in vis:
      continue

    vis.add((y, x))

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      ny, nx = y + dy, x + dx

      if 0 <= ny < H and 0 <= nx < W and ord(grid[ny][nx]) - ord(grid[y][x]) <= 1:
          q.append((ny, nx, c + 1))

print(solve(1))
print(solve(2))