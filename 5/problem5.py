def load_data() -> list:
    moves = []

    with open("problem5.txt", "r") as file:
        for line in file:
            split_line = line.rstrip("\n").split(" ")

            move = {
                "move": int(split_line[1]),
                "from": split_line[3],
                "to": split_line[5]
            }

            moves.append(move)

        return moves

def sort_crates(moves: list):

    crate_stacks = {
        "1": ['B', 'V', 'S', 'N', 'T', 'C', 'H', 'Q'],
        "2": ['W', 'D', 'B', 'G'],
        "3": ['F', 'W', 'R', 'T', 'S', 'Q', 'B'],
        "4": ['L', 'G', 'W', 'S', 'Z', 'J', 'D', 'N'],
        "5": ['M', 'P', 'D', 'V', 'F'],
        "6": ['F', 'W', 'J'],
        "7": ['L', 'N', 'Q', 'B', 'J', 'V'],
        "8": ['G', 'T', 'R', 'C', 'J', 'Q', 'S', 'N'],
        "9": ['J', 'S', 'Q', 'C', 'W', 'D', 'M']
    }

    """

    # Part 1

    for move in moves:
        number_to_move = move["move"]
        from_stack = move["from"]
        to_stack = move["to"]

        for i in range(0, number_to_move):
            stack = crate_stacks[from_stack].pop()
            crate_stacks[to_stack].append(stack)
    """

    # Part 2
    
    for move in moves:
        number_to_move = move["move"]
        from_stack = move["from"]
        to_stack = move["to"]

        index = number_to_move

        moved_crates = crate_stacks[from_stack][-index:]

        del crate_stacks[from_stack][-index:]

        crate_stacks[to_stack] = crate_stacks[to_stack] + moved_crates

data = load_data()
sort_crates = sort_crates(data)