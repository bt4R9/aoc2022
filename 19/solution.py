import re
import collections
from copy import deepcopy

lines = [x.split(':')[1] for x in open('input', 'r').read().split('\n')]
blue_prints = []

for line in lines: 
  [*args, _] = line.split('.')
  blue_prints.append([list(map(int, re.findall('[0-9]+', arg))) for arg in args])

class State:
  def __init__(self, costs):
    self.r_ore = 1
    self.r_clay = 0
    self.r_obsidian = 0
    self.r_geode = 0
    self.ore = 0
    self.clay = 0
    self.obsidian = 0
    self.geode = 0
    self.minutes = 0

    self.costs = costs

  def collect(self):
    self.ore += self.r_ore
    self.clay += self.r_clay
    self.obsidian += self.r_obsidian
    self.geode += self.r_geode

  def buy(self, robot):
    if robot == "ore":
      self.r_ore += 1
      self.ore -= self.costs["ore"]["ore"]
    elif robot == "clay":
      self.r_clay += 1
      self.ore -= self.costs["clay"]["ore"]
    elif robot == "obsidian":
      self.r_obsidian += 1
      self.ore -= self.costs["obsidian"]["ore"]
      self.clay -= self.costs["obsidian"]["clay"]
    elif robot == "geode":
      self.r_geode += 1
      self.ore -= self.costs["geode"]["ore"]
      self.obsidian -= self.costs["geode"]["obsidian"]

  def can_buy(self):
    return [
      self.ore >= self.costs["ore"]["ore"],
      self.ore >= self.costs["clay"]["ore"],
      self.ore >= self.costs["obsidian"]["ore"] and self.clay >= self.costs["obsidian"]["clay"],
      self.ore >= self.costs["geode"]["ore"] and self.obsidian >= self.costs["geode"]["obsidian"] 
    ]

  def key(self):
    return (
      self.minutes,
      self.ore,
      self.clay,
      self.obsidian,
      self.geode,
      self.r_ore,
      self.r_clay,
      self.r_obsidian,
      self.r_geode
    )

def calculate(blue_print, time):
  costs = {
    "ore": { "ore": blue_print[0][0] },
    "clay": { "ore": blue_print[1][0] },
    "obsidian": { "ore": blue_print[2][0], "clay": blue_print[2][1] },
    "geode": { "ore": blue_print[3][0], "obsidian": blue_print[3][1] }
  }

  q = collections.deque([State(costs)])
  visited = set()
  ans = []

  best_geode = collections.defaultdict(int)

  while q:
    state = q.popleft()
    key = state.key()

    if key in visited:
      continue

    visited.add(key)
    state.minutes += 1

    if state.minutes > time:
      ans.append(state.geode)
      continue

    [cb_ore, cb_clay, cb_obsidian, cb_geode] = state.can_buy()

    # other optimization? tooooo slow

    # we spend resources before collecting
    state.collect()

    # no reason to explore other options if we can buy geode
    if cb_geode:
      s = deepcopy(state)
      s.buy("geode")
      q.append(s)
      continue

    q.append(state)

    if cb_obsidian and state.r_obsidian < costs["geode"]["obsidian"]:
      s = deepcopy(state)
      s.buy("obsidian")
      q.append(s)

    if cb_clay and state.r_clay < costs["obsidian"]["clay"]:
      s = deepcopy(state)
      s.buy("clay")
      q.append(s)

    if cb_ore and state.r_ore < max([costs["ore"]["ore"], costs["clay"]["ore"], costs["obsidian"]["ore"], costs["geode"]["ore"]]):
      s = deepcopy(state)
      s.buy("ore")
      q.append(s)

  return max(ans)

def solve(part):
  if part == 1:
    sums = []
    for i, blue_print in enumerate(blue_prints):
      sums.append(calculate(blue_print, 24) * (i + 1))
    print(sum(sums))

  if part == 2:
    prod = 1
    for blue_print in blue_prints[:3]:
      prod *= calculate(blue_print, 32)
    print(prod)

solve(1)
# solve(2)