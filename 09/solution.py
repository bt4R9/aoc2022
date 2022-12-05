commands = [x.split(' ') for x in open('input', 'r').read().split('\n')]
dirs = { "R": (0, 1), "L": (0, -1), "U": (1, 0), "D": (-1, 0) }

def move_H(H, cmd):
  (y, x), (dy, dx) = H, dirs[cmd]
  return (y + dy, x + dx)

def move_T(H, T):
  (hy, hx), (ty, tx) = H, T
  dy, dx, diff_y, diff_x = 0, 0, hy - ty, hx - tx

  if diff_x == 0 and abs(diff_y) == 2:
	  dy = diff_y // 2
  elif abs(diff_x) == 2 and diff_y == 0:
	  dx = diff_x // 2
  elif (abs(diff_x) + abs(diff_y)) > 2:
    dy, dx =  diff_y // abs(diff_y), diff_x // abs(diff_x)

  return ty + dy, tx + dx

T, H = (0, 0), (0, 0)
path = set()

for dir, num in commands:
  for _ in range(int(num)):
    H = move_H(H, dir)
    T = move_T(H, T)
    path.add(T)

print("part 1", len(path))

H, T = (0, 0), [(0, 0)] * 9
path = set()
path.add((0, 0))

def move_Ts(H, T):
  T[0] = move_T(H, T[0])
  for i in range(1, 9):
    T[i] = move_T(T[i - 1], T[i])

for dir, num in commands:
  for _ in range(int(num)):
    H = move_H(H, dir)
    move_Ts(H, T)
    path.add(T[8])

print("part 2", len(path))