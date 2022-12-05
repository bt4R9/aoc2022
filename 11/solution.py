from collections import deque

blocks = open('input', 'r').read().split('\n\n')
monkeys = [{} for _ in range(len(blocks))]

def calc(op, old):
  match op:
    case ["old", "*", "old"]:
      return old * old
    case ["old", "+", "old"]:
      return old + old
    case ["old", "*", *n]:
      return old * int(n[0])
    case ["old", "+", *n]:
      return old + int(n[0])

def solve(part):
  for i, block in enumerate(blocks):
    groups = block.split('\n')

    monkeys[i]['index'] = i
    monkeys[i]['queue'] = deque([int(x.strip()) for x in groups[1].split(':')[1].split(',')])
    monkeys[i]['op'] = groups[2].strip().split(' ')[3:]
    monkeys[i]['test'] = int(groups[3].strip().split(' ')[-1])
    monkeys[i]['true'] = int(groups[4].strip().split(' ')[-1])
    monkeys[i]['false'] = int(groups[5].strip().split(' ')[-1])
    monkeys[i]['inspects'] = 0

  divs = [x['test'] for x in monkeys]
  modulo = 1
  for i in divs:
    modulo *= i

  for _ in range(20 if part == 1 else 10000):
    for i, monkey in enumerate(monkeys):
      while monkey['queue']:
        level = monkey['queue'].popleft()
        worry = calc(monkey['op'], level)
        calm = int(worry // 3) if part == 1 else worry % modulo
        test = calm % monkey['test'] == 0
        if test:
          monkeys[monkey['true']]['queue'].append(calm)
        else:
          monkeys[monkey['false']]['queue'].append(calm)
        monkey['inspects'] += 1

  result = sorted([x['inspects'] for x in monkeys])
  return result[-1] * result[-2]

print(solve(1))
print(solve(2))