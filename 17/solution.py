from collections import defaultdict

winds = open("input", "r").read()

def shape_to_points(shape):
  points = []
  for y in range(len(shape)):
    for x in range(len(shape[y])):
      if shape[y][x] == "#":
        points.append((y, x))
  return points

shapes = list(map(shape_to_points, [
  ['####'],
  ['.#.', '###', '.#.'],
  ['###', '..#', '..#'], # <- opposite
  ['#', '#', '#', '#'],
  ['##', '##'],
]))

tower_width = 7
shapes_width = len(shapes)
winds_width = len(winds)

def in_bound(shape):
  for y, x in shape:
    if not 0 <= x < tower_width:
      return False
  return True

def in_tower(tower, shape):
  for point in shape:
    if point in tower:
      return True
  return False

def free_memory(tower, scale):
  max_y = float("-inf")
  min_y = float("inf")

  for y, x in tower:
    max_y = max(max_y, y)
    min_y = min(min_y, y)

  for y in range(min_y, max_y - scale):
    for x in range(tower_width):
      if (y, x) in tower:
        tower.remove((y, x))

wind_index = 0
tower = set([(0, x) for x in range(tower_width)])

for sim_index in range(100000):
  shape = shapes[sim_index % shapes_width]
  dy, dx = max(y for y, x in tower) + 4, 2
  S = [(y + dy, x + dx) for y, x in shape]

  while True:
    wind = winds[wind_index % winds_width]
    wind_index += 1
    dy, dx = -1, -1 if wind == "<" else 1

    newS = [(y, x + dx) for y, x in S]
    if in_bound(newS) and not in_tower(tower, newS):
      S = newS

    newS = [(y - 1, x) for y, x in S]
    if in_tower(tower, newS):
      tower.update(S)
      break

    S = newS

  if sim_index % 1720 == 0:
    free_memory(tower, 1720)

max_y = max(y for y, x in tower)
print(max_y)
