from collections import defaultdict
from copy import deepcopy

moves = {
  "N": (-1, 0), "S": (1, 0), "NW": (-1, -1), "SW": (1, -1),
  "W": (0, -1), "E": (0, 1), "NE": (-1, 1),  "SE": (1, 1),
}
dirs8 = ["N", "S", "W", "E", "NW", "NE", "SW", "SE"]
dirs4 = ["N", "S", "W", "E"]
dirs = {
  "N": ["N", "NW", "NE"],
  "S": ["S", "SW", "SE"],
  "W": ["W", "NW", "SW"],
  "E": ["E", "NE", "SE"]
}

def elfs_around(board, point):
  y, x = point
  elfs = set()
  for d in dirs8:
    dy, dx = moves[d]
    ny, nx = y + dy, x + dx
    if (ny, nx) in board:
      elfs.add(d)
  return elfs

def get_new_dir(elfs):
  for d in dirs4:
    flag = True
    for dd in dirs[d]:
      if dd in elfs:
        flag = False
    if flag:
      return d
  return None

def calculate_empty_in_square(board):
  miny, maxy = float("inf"), float("-inf")
  minx, maxx = float("inf"), float("-inf")

  for (y, x) in board:
    miny = min(miny, y)
    maxy = max(maxy, y)
    minx = min(minx, x)
    maxx = max(maxx, x)

  return (maxy - miny + 1) * (maxx - minx + 1) - len(board)

def solve1():
  raw = [list(x) for x in open('input', 'r').read().strip().split('\n')]
  H, W  = len(raw), len(raw[0])
  board = {}

  for y in range(H):
    for x in range(W):
      if raw[y][x] == "#":
        board[(y, x)] = "#"

  rounds = 10

  for i in range(rounds):
    patches = defaultdict(list)

    for (y, x) in board:
      elfs = elfs_around(board, (y, x))

      if len(elfs) > 0:
        newd = get_new_dir(elfs)

        if newd:
          dy, dx = moves[newd]
          ny, nx = y + dy, x + dx
          patches[(ny, nx)].append((y, x))

    if len(patches) > 0:
      newboard = deepcopy(board)

      for point, patch in patches.items():
        if len(patch) > 1:
          continue

        py, px = patch[0]
        y, x = point

        newboard.pop((py, px))
        newboard[(y, x)] = "#"

      board = newboard

    dirs4.append(dirs4.pop(0))

  print(calculate_empty_in_square(board))

def solve2():
  raw = [list(x) for x in open('input', 'r').read().strip().split('\n')]
  H, W  = len(raw), len(raw[0])
  board = {}

  for y in range(H):
    for x in range(W):
      if raw[y][x] == "#":
        board[(y, x)] = "#"

  rounds = 0

  while True:
    rounds += 1
    patches = defaultdict(list)

    for (y, x) in board:
      elfs = elfs_around(board, (y, x))

      if len(elfs) > 0:
        newd = get_new_dir(elfs)

        if newd:
          dy, dx = moves[newd]
          ny, nx = y + dy, x + dx
          patches[(ny, nx)].append((y, x))

    c = 0

    if len(patches) > 0:
      newboard = deepcopy(board)

      for point, patch in patches.items():
        if len(patch) > 1:
          continue

        c += 1
        py, px = patch[0]
        y, x = point
        newboard.pop((py, px))
        newboard[(y, x)] = "#"

      board = newboard

    dirs4.append(dirs4.pop(0))

    if c == 0:
      break

  print(rounds)

solve1()
solve2()