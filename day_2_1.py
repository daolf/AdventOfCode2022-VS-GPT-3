rules = {
    "R": "S",
    "P": "R",
    "S": "P",
}

with open("input_day_2.txt") as f:
    guide = f.readlines()

total_score = 0

for line in guide:
    shapes = line.strip().split()
    first_shape = shapes[0]
    second_shape = shapes[1]

    # Replace letters in strategy guide with letters in rules dictionary
    first_shape = first_shape.replace("A", "R").replace("B", "P").replace("C", "S")
    second_shape = second_shape.replace("A", "R").replace("B", "P").replace("C", "S")

    # Calculate scores for each player
    if first_shape == second_shape:
        # Round ends in a draw
        first_score = 1 + 3
        second_score = 1 + 3
    elif rules[first_shape] == second_shape:
        # First player wins
        first_score = 1 + 6
        second_score = 1 + 0
    else:
        # Second player wins
        first_score = 1 + 0
        second_score = 1 + 6

    total_score += first_score + second_score

print(total_score)
