nums = [int(x) for x in open('input', 'r').read().split('\n')]

class Node:
  def __init__(self, val, multiplier):
    self.val = val * multiplier
    self.prev = None
    self.next = None

def insertAfter(node, after):
  next = after.next

  node.next = next
  node.prev = after

  after.next = node
  next.prev = node

def insertBefore(node, before):
  prev = before.prev

  node.prev = prev
  node.next = before

  prev.next = node
  before.prev = node

def calculate(times = 1, multiplier = 1):
  process = []
  head = Node(0, multiplier)
  p = head

  for n in nums:
    node = Node(n, multiplier)
    process.append(node)
    p.next = node
    node.prev = p
    p = node

  node.next = head.next
  head.next.prev = node

  for _ in range(times):
    for node in process:
      if node.val == 0:
        continue

      prev = node.prev
      next = node.next

      prev.next = next
      next.prev = prev

      l = (abs(node.val) - 1) % (len(process) - 1)

      if node.val > 0:
        p = next
        for _ in range(l):
          p = p.next

        insertAfter(node, p)

      elif node.val < 0:
        p = prev
        for _ in range(l):
          p = p.prev

        insertBefore(node, p)

  zero = None

  for n in process:
    if n.val == 0:
      zero = n
      break

  t1, t2, t3 = None, None, None

  for i in range(1, 3001):
    zero = zero.next

    if i == 1000:
      t1 = zero
    if i == 2000:
      t2 = zero
    if i == 3000:
      t3 = zero

  print(sum([t1.val, t2.val, t3.val]))

calculate()
calculate(10, 811589153)