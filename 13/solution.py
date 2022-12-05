groups = [[eval(group) for group in pair.split('\n')] for pair in open('input', 'r').read().split('\n\n')]

def check(g1, g2):
  if isinstance(g1, int) and isinstance(g2, int):
    if g1 == g2:
      return None
    elif g1 < g2:
      return True
    elif g1 > g2:
      return False

  if isinstance(g1, list) and isinstance(g2, list):
    for n1, n2 in zip(g1, g2):
      res = check(n1, n2)

      if res is not None:
        return res

    l1, l2 = len(g1), len(g2)

    if l1 == l2:
      return None
    elif l1 < l2:
      return True
    elif l1 > l2:
      return False

  if isinstance(g1, int):
    return check([g1], g2)
  elif isinstance(g2, int):
    return check(g1, [g2])

  return None

ans = 0
p1, p2 = 0, 0

for i, (g1, g2) in enumerate(groups):
  if check(g1, g2):
    ans += i + 1

  if check(g1, [[2]]):
    p1 += 1
  if check(g2, [[2]]):
    p1 += 1

  if check(g1, [[6]]):
    p2 += 1
  if check(g2, [[6]]):
    p2 += 1

print(ans)
print((p1 + 1) * (p2 + 2))
