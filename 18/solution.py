import collections
import sys
sys.setrecursionlimit(10000)

xyz = [tuple([int(x) for x in line.split(',')]) for line in open('input', 'r').read().split('\n')]
pos = set(xyz)
dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
ans = 0

for x, y, z in xyz:
  for dx, dy, dz in dirs:
    if (x + dx, y + dy, z + dz) not in pos:
      ans += 1 
    
print(ans)

ans = 0
size = max([max(p) for p in xyz])
low, high = -1, size + 2
p = (size - 1, size - 1, size - 1)
seen = set([p])
q = collections.deque([p])

while q:
  x, y, z = q.popleft()

  for dx, dy, dz in dirs:
    nx, ny, nz = x + dx, y + dy, z + dz
    if (nx, ny, nz) in seen:
      continue
    if (nx, ny, nz) in pos:
      continue
    if not low <= x < high or not low <= y < high or not low <= z < high:
      continue

    q.append((nx, ny, nz))
    seen.add((nx, ny, nz))

for x, y, z in xyz:
    for dx, dy, dz in dirs:
      nx, ny, nz = x + dx, y + dy, z + dz

      if (nx, ny, nz) in seen:
        ans += 1

print(ans)