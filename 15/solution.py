import re
input = open('input', 'r').read().split('\n')

def solve(part):
  sensors = set()
  beacons = set()
  empty = set()
  points = []

  for line in input:
    m = re.search(r'Sensor at x=([-0-9]+), y=([-0-9]+): closest beacon is at x=([-0-9]+), y=([-0-9]+)', line)
    sx, sy = int(m.group(1)), int(m.group(2))
    bx, by = int(m.group(3)), int(m.group(4))
    sensors.add((sy, sy))
    beacons.add((bx, by))
    points.append((sx, sy, bx, by))

  if part == 1:
    y = 2000000

    for sx, sy, bx, by in points:
      r = abs(bx - sx) + abs(by - sy)
      dist = abs(sy - y)

      if dist <= r:
        for x in range(sx - (r - dist), sx + (r - dist) + 1):
          if not (x, y) in beacons:
            empty.add((x, y))

    return len(empty)

  if part == 2:
    ranges = [[] for _ in range(4000000 + 1)]
    for sx, sy, bx, by in points:
      for y, rng in enumerate(ranges):
        r = abs(bx - sx) + abs(by - sy)
        dist = r - abs(sy - y)
        if dist >= 0:
          rng.append((sx - dist, sx + dist))
          if by == y:
            rng.append((bx, bx))

    for y, rng in enumerate(ranges):
      bounds = sorted(rng, key=lambda x: x[0])
      n = 0
      for x, y in bounds:
        if x <= n and y >= n:
          n = y + 1
      if n <= 4000000:
        return n * 4000000 + y


print(solve(1))
print(solve(2))
