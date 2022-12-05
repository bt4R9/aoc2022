from collections import deque
input = open('input', 'r').read().split('\n')

class Node:
  def __init__(self, ntype):
    self.name = ""
    self.parent = None
    self.children = []
    self.type = ntype
    self.size = 0

class Tree:
  def __init__(self):
    self.root = Node("dir")
    self.root.name = "root"
    self.sizes = {}

  def key(self, node):
    parts = deque()

    while node:
      parts.appendleft(node.name)
      node = node.parent

    return "/".join(list(parts))

  def build(self, lines):
    p = self.root

    for line in lines:
      parts = line.split(' ')
      p0, p1 = parts[0], parts[1]

      if p0 == "$" and p1 == "cd":
        p2 = parts[2]
        if p2 == "/":
          p = self.root
        elif p2 == "..":
          p = p.parent
        else:
          p = next(node for node in p.children if node.name == p2)
      elif p0 == "dir":
        node = Node("dir")
        node.name = p1
        node.parent = p

        p.children.append(node)
      elif str(p0).isnumeric():
        node = Node("file")
        node.size = int(p0)
        p.children.append(node)

  def calc_size(self):
    def dfs(node):
      if not node:
        return 0

      if node.type == "file":
        return node.size

      if node.type == "dir":
        s = 0

        for child in node.children:
          s += dfs(child)

        node.size = s
        self.sizes[self.key(node)] = s

        return s

    dfs(self.root)

tree = Tree()
tree.build(input)
tree.calc_size()

# part 1
print(sum(x for x in tree.sizes.values() if x < 100_100))

# part 2
lookup = 30_000_000 - (70_000_000 - tree.sizes["root"])
print(min([d for d in tree.sizes.values() if d >= lookup]))
