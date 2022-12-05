input = [x.split(' ') for x in open('input', 'r').read().split('\n')]

x = 1
cycle = 0
cycles = set([20, 60, 100, 140, 180, 220])
screen = []
row = ""
ans = 0

for line in input:
  cmd = line[0]

  if cmd == "noop":
    cycle += 1
    row += "#" if x - 1 <= len(row) <= x + 1 else "."

    if len(row) == 40:
      screen.append(row)
      row = ""

    if cycle in cycles:
      ans += x * cycle

  elif cmd == "addx":
    for _ in range(2):
      cycle += 1
      row += "#" if x - 1 <= len(row) <= x + 1 else "."

      if len(row) == 40:
        screen.append(row)
        row = ""

      if cycle in cycles:
        ans += x * cycle

    x += int(line[1])

print(ans)

for row in screen:
  print(row)