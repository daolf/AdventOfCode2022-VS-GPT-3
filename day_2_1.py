# Read the input file
with open('input_day_2.txt') as f:
    strategy = f.read().strip().split('\n')

# Define a dictionary that maps each shape to its score
score = {
    'A': 1,  # Rock
    'B': 2,  # Paper
    'C': 3,  # Scissors
}

# Define a dictionary that maps each outcome to its score
outcome = {
    'L': 0,  # Lost
    'D': 3,  # Draw
    'W': 6,  # Won
}

# Initialize the total score to 0
total_score = 0

# Loop over the strategy guide and simulate the game
for line in strategy:
    # Parse the strategy guide
    opponent, result = line.split()

    # Simulate the round and update the total score
    total_score += score[opponent] + outcome[result]

# Print the total score
print(total_score)
