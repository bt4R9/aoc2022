paths = open('input', 'r').read().split('\n')

def solve(part):
  grid = {}

  for path in paths:
    parts = [[int(x) for x in point.strip().split(',')] for point in path.split('->')]

    for i in range(1, len(parts)):
      x0, y0 = parts[i - 1]
      x1, y1 = parts[i]

      for x in range(min(x0, x1), max(x0, x1) + 1):
        for y in range(min(y0, y1), max(y0, y1) + 1):
          grid[(x, y)] = '#'

  R, B = max([x[0] for x in grid.keys()]), max([x[1] for x in grid.keys()])

  if part == 2:
    B += 2
    for x in range(0, B ** 2):
      grid[(x, B)] = "#"

  while True:
    x, y = 500, 0
    moving = True

    while True:
      if part == 1 and x > R or y > B:
        break
      elif not (x, y + 1) in grid:
        y = y + 1
      elif not (x - 1, y + 1) in grid:
        x, y = x - 1, y + 1
      elif not (x + 1, y + 1) in grid:
        x, y = x + 1, y + 1
      else:
        grid[(x, y)] = "O"
        break

    if part == 1 and x > R or y > B:
      break

    if part == 2 and x == 500 and y == 0:
      break

  return sum([1 for value in grid.values() if value == "O"])

print(solve(1))
print(solve(2))
