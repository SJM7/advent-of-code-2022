import string

def load_data() -> list:
    """ Loads data and formats """

    with open('problem3.txt', 'r') as file:
        data = [line.rstrip('\n') for line in file]

        return data

def score_rucksack(rucksacks: list) -> int:
    """ Scores a a set of rucksacks for each part """

    priorities = {}

    alphabet = list(string.ascii_lowercase)

    for i in range(0, len(alphabet)):
        index = i + 1
        letter = alphabet[i]
        upper_case = letter.upper()

        priorities[letter] = index
        priorities[upper_case] = index + 26

    """

    # Part 1 logic

    # Change function parameter back to rucksack and type string, to accept single item

    priority_sum = set()

    first, second = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]

    for letter in first:
        if letter in second:
            priority_sum.add(priorities[letter])

    return priority_sum

    """

    # Part 2 logic

    priority_sum = []

    for i in range(0, len(rucksacks), 3):
        chunk = rucksacks[i:i+3]

        first = set(chunk[0])
        second = set(chunk[1])
        third = set(chunk[2])

        intersection = first & second & third

        for letter in intersection:
            priority_sum.append(priorities[letter])

    total = sum(priority_sum)

    print('Total: ', total)

data = load_data()
scores = []

"""

# part 1

for rucksack in data:
    score = score_rucksack(rucksack)

    scores.append(sum(score))

total = sum(scores)

print('Total: ', total)

"""

score_rucksack(data)
