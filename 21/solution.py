lines = [line.split(':') for line in open('input', 'r').read().strip().split('\n')]
monkeys = {key: value for key, value in lines}

def calculate(monkey, high):
  if monkey == 'humn' and high > 0:
    return high

  value = monkeys[monkey].strip()

  if str(value).isnumeric():
    return int(value)

  [m1, op, m2] = value.split(' ')

  m1 = calculate(m1, high)
  m2 = calculate(m2, high)

  if op == '*':
    return m1 * m2
  elif op == '+':
    return m1 + m2
  elif op == '/':
    return m1 / m2
  elif op == '-':
    return m1 - m2

print(int(calculate('root', 0)))

[search_monkey, _, target_monkey] = monkeys['root'].strip().split(' ')
 
if calculate(target_monkey, 0) != calculate(target_monkey, 1):
  # swap
  search_monkey, target_monkey = target_monkey, search_monkey

target = calculate(target_monkey, 0)

# r = 1e15
l, r = 0, 1_000_000_000_000_000
1e
while l < r:
  mid = l + ((r - l) // 2)
  res = target - calculate(search_monkey, mid)

  if res == 0:
    print(int(mid))
    break
  
  elif res < 0:
    l = mid
  else:
    r = mid