def find_top_elves(input_file):
    # Create a dictionary to store the calories for each elf
    elf_calories = {}

    # Open the input file
    with open(input_file, 'r') as f:
        # Read the first line of the input file
        line = f.readline()

        # Keep track of the current elf's name
        current_elf = "Elf 1"

        # Read the input file line by line
        while line:
            # If the line is empty, move on to the next elf
            if line.strip() == "":
                current_elf = "Elf " + str(int(current_elf.split()[1]) + 1)

            # Otherwise, add the calories to the current elf's total
            else:
                if current_elf in elf_calories:
                    elf_calories[current_elf] += int(line)
                else:
                    elf_calories[current_elf] = int(line)

            # Read the next line
            line = f.readline()

    # Sort the elves by their calorie count in descending order
    sorted_elves = sorted(elf_calories.items(), key=lambda x: x[1], reverse=True)

    # Return the top three elves
    return sorted_elves[:3]


# Find the top three elves
top_elves = find_top_elves("input_day_1.txt")

# Sum the calorie counts for the top three elves
total_calories = 0
for elf, calories in top_elves:
  total_calories += calories

# Print the total calories carried by the top three elves
print(total_calories)
