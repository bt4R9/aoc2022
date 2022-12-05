input = open('input', 'r').read().split('\n')

# part 1
ans = 0

for line in input:
    half = len(line) // 2
    diff = set(line[:half]) & set(line[half:])
    o = ord(list(diff)[0])
    ans += o - 96 if o >= 97 else o - 38

print(ans)


# part 2
ans = 0

for i in range(0, len(input), 3):
    diff = set(input[i]) & set(input[i + 1]) & set(input[i + 2])
    o = ord(list(diff)[0])
    ans += o - 96 if o >= 97 else o - 38

print(ans)
