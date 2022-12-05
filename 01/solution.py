import heapq

input = open('input', 'r').read()

nums = input.split("\n\n")
groups = [sum([int(x) for x in group.split("\n")]) for group in nums]

# part 1
part1 = max(groups)

# part 2
heap = [-x for x in groups]
heapq.heapify(heap)
part2 = sum([-heapq.heappop(heap) for _ in range(3)])

print(part1, part2)
