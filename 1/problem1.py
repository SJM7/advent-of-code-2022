elf_calories = []

with open('problem1.txt', 'r') as file:
    calories = 0

    for line in file:
        if line != '\n':

            calories = calories + int(line[:-1])

        else:

            elf_calories.append(calories)

            calories = 0

#part 1
max_calories = max(elf_calories)

print('Maximum calories: ', max_calories)

# part 2
elf_calories.sort(reverse=True)

top_3_calories = sum(elf_calories[0:3])

print('Top 3 calories summed: ', top_3_calories)
