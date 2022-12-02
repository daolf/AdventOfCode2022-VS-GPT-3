def find_hungriest_elf(input_file):
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

    # Find the elf with the most calories
    hungriest_elf = None
    most_calories = 0
    for elf, calories in elf_calories.items():
        if calories > most_calories:
            hungriest_elf = elf
            most_calories = calories

    # Return the name of the elf with the most calories and their calorie count
    return hungriest_elf, most_calories

hungriest_elf, most_calories = find_hungriest_elf("input_day_1.txt")
print(most_calories)  # This will print the number of total calories carried by the hungriest elf