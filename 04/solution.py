input = open('input', 'r').read().split('\n')
lines = [x.split(',') for x in input]
pairs = [[map(int, x.split('-')) for x in pair] for pair in lines]

ans = 0

# part 1
for ((a0, a1), (b0, b1)) in pairs:
    if (a0 <= b0 and a1 >= b1) or (a0 >= b0 and a1 <= b1):
        ans += 1

print(ans)

ans = 0

# part 2
for ((a0, a1), (b0, b1)) in pairs:
    if (a0 <= b0 <= a1) or (a0 <= b1 <= a1) or (b0 <= a0 <= b1) or (b0 <= a1 <= b1):
        ans += 1

print(ans)
