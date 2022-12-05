input = open('input').read()
lines = [x.split(" ") for x in input.split('\n')]

rules = {
    ("A", "A"): 3,
    ("A", "B"): 0,
    ("A", "C"): 6,

    ("B", "A"): 6,
    ("B", "B"): 3,
    ("B", "C"): 0,

    ("C", "A"): 0,
    ("C", "B"): 6,
    ("C", "C"): 3,
}

values = {
    "A": 1,
    "B": 2,
    "C": 3,
}

convert = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

ends = {
    "X": 0,
    "Y": 3,
    "Z": 6
}


def getCorrectHand(op, ending):
    if ending == "X":
        if op == "A":
            return "C"
        if op == "B":
            return "A"
        if op == "C":
            return "B"

    if ending == "Y":
        return op

    if ending == "Z":
        if op == "A":
            return "B"
        if op == "B":
            return "C"
        if op == "C":
            return "A"


score = 0

for (op, ending) in lines:
    hand = getCorrectHand(op, ending)
    score += values.get(hand) + ends.get(ending)

print(score)

# A - Rock
# B - Paper
# C - Scissors

# B > A
# A > C
# C > B
