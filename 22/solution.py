import math
[raw_board, raw_instructions] = open("input", "r").read().split("\n\n")
raw_board = raw_board.split("\n")
H, W = len(raw_board), len(raw_board[0])
edges = [(0, 50), (0, 100), (50, 50), (100, 50), (100, 0), (150, 0)]
size = 50
T, B, R, L = (1, 0), (-1, 0), (0, 1), (0, -1)

def parse_board(raw):
  grid = {}

  for y in range(len(raw_board)):
    for x in range(len(raw_board[y])):
      if raw[y][x] != " ":
        grid[(y, x)] = raw[y][x]

  return grid

def get_side(point):
  y, x = point

  if 0 <= y < size:
    if size <= x < size * 2:
      return 0
    if size * 2 <= x < size * 3:
      return 1

  if size <= y < size * 2:
    if size < x <= size * 2:
      return 2

  if size * 2 <= y < size * 3:
    if size <= x < size:
      return 3
    if 0 <= x < size:
      return 4

  if size * 3 <= y < size * 4:
    if 0 <= x < size:
      return 5

  assert("impossible")

def teleport(grid, point, d):
  y, x = point
  dy, dx = d
  side = get_side((y, x))
  ndy, ndx, nside = 0, 0, -1

  if (dy, dx) == T:
    if side == 1:
      nside = 3
      ndy, ndx = L
    elif side == 3:
      nside = 6
      ndy, ndx = L
    elif side == 5:
      nside = 2
      ndy, ndx = T

    assert("impossible!")

  if (dy, dx) == R:
    if side == 1:
      nside = 4
      ndy, ndx = L
    elif side == 2:
      nside = 2
      ndy, ndx = B
    elif side == 3:
      nside = 2
      ndy, ndx = L
    elif side == 5:
      nside = 4
      ndy, ndx = B

    assert("impossible")

  if (dy, dx) == B:
    if side == 0:
      nside = 6
      ndy, ndx = R
    elif side == 1:
      nside = 6
      ndy, ndx = B
    elif side == 4:
      nside = 3
      ndy, ndx = R

    assert("impossible")

  if (dy, dx) == L:
    if side == 0:
      nside = 5
      ndy, ndx = R
    elif side == 2:
      nside = 5
      ndy, ndx = T
    elif side == 4:
      nside = 1
      ndy, ndx = R
    elif side == 5:
      nside = 1
      ndy, ndx = T

    assert("impossible")

  p2d = {
    T: "T",
    B: "B",
    R: "R",
    L: "L"
  }

  dirs = {
    "R": 0,
    "T": 1,
    "L": 2,
    "B": 3
  }

  oldDir = dirs[p2d[(dy, dx)]]
  newDir = dirs[p2d[(ndy, ndx)]]
  ry, rx = y - edges[side][0], x - edges[side][1]

  if abs(oldDir - newDir) % 2 == 0:
    ry, rx = 49 - ry, rx
  else:
    ry, rx = rx, ry

  ey = edges[nside - 1][0] + ry
  ex = edges[nside - 1][1] + rx

  return ey, ex, ndy, ndx

def get_start_position(raw):
  for x in range(W):
    if raw[0][x] == ".":
      return (0, x)

def parse_instructions(raw):
  data = []
  num = ""

  for char in raw:
    if str(char).isnumeric():
      num += char
    else:
      data.append(int(num))
      data.append(char)
      num = ""

  if num:
    data.append(int(num))

  return data

def turn(dir, angle):
  y, x = dir
  if angle == "R":
    return (x, -y)
  if angle == "L":
    return (-x, y)

def find_opposite_point(grid, point, d):
  y, x = point
  dy, dx = d

  if dy > 0:
    for ny in range(0, y):
      if (ny, x) in grid and grid[(ny, x)] != " ":
        return (ny, x)
  if dy < 0:
    for ny in range(H - 1, -1, -1):
      if (ny, x) in grid and grid[(ny, x)] != " ":
        return (ny, x)
  if dx > 0:
    for nx in range(0, x):
      if (y, nx) in grid and grid[(y, nx)] != " ":
        return (y, nx)
  if dx < 0:
    for nx in range(W - 1, -1, -1):
      if (y, nx) in grid and grid[(y, nx)] != " ":
        return (y, nx)  

def solve_part1():
  grid = parse_board(raw_board)
  instructions = parse_instructions(raw_instructions)

  y, x = get_start_position(raw_board)
  dy, dx = 0, 1

  for instruction in instructions:
    if instruction == "L" or instruction == "R":
      dy, dx = turn((dy, dx), instruction)
    else:
      for _ in range(instruction):
        ny, nx = y + dy, x + dx
        if (ny, nx) in grid:
          if grid[(ny, nx)] == "#":
            break
        else:
          ny, nx = find_opposite_point(grid, (y, x), (dy, dx))
          if grid[(ny, nx)] == "#":
            break

        y, x = ny, nx

  facing = 0
  if (dy, dx) == (0, 1):
    facing = 0
  if (dy, dx) == (1, 0):
    facing = 1
  if (dy, dx) == (0, -1):
    facing = 2
  if (dy, dx) == (-1, 0):
    facing = 3

  print(1000 * (y + 1) + 4 * (x + 1) + facing)

def solve_part2():
  grid = parse_board(raw_board)
  instructions = parse_instructions(raw_instructions)
  y, x = get_start_position(raw_board)
  dy, dx = 0, 1

  for instruction in instructions:
    if instruction == "L" or instruction == "R":
      dy, dx = turn((dy, dx), instruction)
    else:
      for _ in range(instruction):
        ny, nx = y + dy, x + dx
        in_grid = (ny, nx) in grid

        if in_grid and grid[(ny, nx)] == "#":
          break

        if (in_grid and grid[(ny, nx)] == " ") or not in_grid:
          ny, nx, ndy, ndx = teleport(grid, (y, x), (dy, dx))

          if grid[(ny, nx)] == "#":
            break

          dy, dx = ndy, ndx

      y, x = ny, nx

  facing = 0
  if (dy, dx) == (0, 1):
    facing = 0
  if (dy, dx) == (1, 0):
    facing = 1
  if (dy, dx) == (0, -1):
    facing = 2
  if (dy, dx) == (-1, 0):
    facing = 3

  print(1000 * (y + 1) + 4 * (x + 1) + facing)

solve_part1()
solve_part2()