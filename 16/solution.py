import re
input = open('input', 'r').read().split('\n')
graph = {}

for line in input:
  m = re.search(r"([A-Z]{2}).*rate=([0-9]+).*valves?\s([A-Z\s,]+)", line)
  graph[m.group(1)] = {
    "rate": int(m.group(2)),
    "children": list(map(lambda x: x.strip(), m.group(3).split(",")))
  }

def bc(cave, opened, time, memo):
  key = cave + str(opened) + str(time)

  if key in memo:
    return memo[key]

  if time <= 0:
    return 0

  guess = 0

  if cave not in opened:
    flow = (time - 1) * graph[cave]["rate"]
    new_opened = tuple(sorted(opened + (cave, )))

    for child in graph[cave]["children"]:
      guess = max(
        max(guess, flow + bc(child, new_opened, time - 2, memo)) if flow != 0 else 0,
        max(guess, bc(child, opened, time - 1, memo))
      )

  memo[key] = guess

  return guess

print(bc("AA", (), 30, {}))

def bc2(cave, opened, time, cache):
  key = cave + str(opened) + str(time)

  if key in cache:
    return cache[key]

  if time <= 0:
    res = bc(cave, (), 26, {})
    cache[key] = res
    return res

  guess = 0

  for child in graph[cave]["children"]:
    guess = max(guess, bc2(child, opened, time - 1, cache))

  if cave not in opened and graph[cave]["rate"] != 0 and time > 0:
    new_opened = tuple(sorted(opened + (cave, )))
    val = (time - 1) * graph[cave]["rate"]

    for child in graph[cave]["children"]:
      guess = max(
        guess,
        val + bc2(child, new_opened, time - 2, cache)
      )

  cache[key] = guess
  return guess

print(bc2("AA", (), 26, {}))