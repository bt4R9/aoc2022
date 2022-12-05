from collections import deque, defaultdict

raw_board = [list(x) for x in open('input', 'r').read().split('\n')]
dirs4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dirs_winds = { ">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0) }
H, W = len(raw_board), len(raw_board[0])
blizzards = defaultdict(set)
walls = set()

for y in range(H):
  for x in range(W):
    if raw_board[y][x] == "#":
      walls.add((y, x))
    elif raw_board[y][x] != ".":
      blizzards[(y, x)].add(raw_board[y][x])

def simulate_blizzards():
  global blizzards
  nblizzards = defaultdict(set)

  for (y, x), winds in blizzards.items():
    for wind in winds:
      dy, dx = dirs_winds[wind]
      ny, nx = y + dy, x + dx
      if (ny, nx) in walls:
        if not 1 <= ny < H - 1:
          ny = 1 if ny == H - 1 else H - 2
        if not 1 <= nx < W - 1:
          nx = 1 if nx == W - 1 else W - 2
      nblizzards[(ny, nx)].add(wind)
  blizzards = nblizzards

def walk(start, end):
  y, x = start
  seen = set()
  q = deque([(y, x, 0)])

  while q:
    simulate_blizzards()
    for _ in range(len(q)):
      y, x, c = q.popleft()
      if (y, x) == end:
        return c
      if (y, x) not in walls and len(blizzards[(y, x)]) == 0:
        q.append((y, x, c + 1))
      for dy, dx in dirs4:
        ny, nx = y + dy, x + dx
        if not 0 <= ny < H or not 0 <= nx < W:
          continue
        if (ny, nx) in walls:
          continue
        if len(blizzards[(ny, nx)]) != 0:
          continue
        if not (ny, nx, c + 1) in seen:
          seen.add((ny, nx, c + 1))
          q.append((ny, nx, c + 1)) 

  assert("impossible")

start_x = [i for i, x in enumerate(raw_board[0]) if x == "."][0]
end_x = [i for i, x in enumerate(raw_board[H - 1]) if x == "."][0]
start, end = (0, start_x), (H - 1, end_x)

c1 = walk(start, end)
c2 = walk(end, start) + 1
c3 = walk(start, end) + 1

print(c1)
print(c1 + c2 + c3)