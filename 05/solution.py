from collections import deque

input = open('input').read().split('\n\n')
creates, insts = [x.split('\n') for x in input]

stacks = [deque() for _ in range(9)]

for y in range(len(creates) - 1):
    for x in range(0, len(creates[0]), 4):
        c = creates[y][x + 1]
        if c != ' ':
            stacks[x / 4].appendleft(c)

for i in insts:
    (_, c, _, f, _, t) = i.split(' ')

    for _ in range(int(c)):
        stacks[int(t) - 1].extend([x for x in stacks[int(f) - 1].pop()])

    # part 2
    # buf = deque()
    # for _ in range(int(c)):
    #     buf.appendleft(stacks[int(f) - 1].pop())
    # stacks[int(t) - 1].extend(buf)

print("".join([x[-1] for x in stacks]))
