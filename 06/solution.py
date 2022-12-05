input = open('input', 'r').read()
l = 0
buf = [0] * 128

for r in range(len(input)):
    buf[ord(input[r])] += 1

    while buf[ord(input[r])] > 1:
        buf[ord(input[l])] -= 1
        l += 1

    # part 1
    # if r - l + 1 == 4:
    #     print(r + 1)
    #     break

    if r - l + 1 == 14:
        print(r + 1)
        break
