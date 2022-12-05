def load_data() -> list:
    """ Loads data and formats """

    formatted_sections = []

    with open('problem4.txt', 'r') as file:

        lines = [line.rstrip('\n') for line in file]

        split_sections = list(map(lambda x: list(map(lambda t: t.split('-'), x.split(',', 1))), lines))

        formatted_sections = list(map(lambda x: list(map(lambda t: list(map(lambda y: int(y), t)), x)), split_sections))

        return formatted_sections

def find_overlaps(sections: list) -> int:
    """ Finds the overlap """

    total_score = 0

    for assignment in sections:

        elf_1_start = assignment[0][0]
        elf_1_end = assignment[0][1]
        elf_2_start = assignment[1][0]
        elf_2_end = assignment[1][1]

        """

        # Part 1

        first = (elf_1_start >= elf_2_start) and (elf_1_end <= elf_2_end)
        second = (elf_2_start >= elf_1_start) and (elf_2_end <= elf_1_end)

        if first or second:
            total_score += 1
        
        """

        # Part 2

        first = max(elf_1_start, elf_2_start)
        second = min(elf_1_end, elf_2_end)

        if first <= second:
            total_score += 1
    
    return total_score

    

data = load_data()
score = find_overlaps(data)

print('Total overlaps: ', score)