def load_rounds() -> list:
    """ Loads rounds and formats, returns a list of rounds """

    with open('problem2.txt', 'r') as file:
        round_number = 1
        rounds = []

        for line in file:
            split_line = line.rstrip('\n').split(' ')

            formatted_round = []

            if '' in split_line:
                next

            else:

                rounds.append(split_line)

                """

                # Used for part 1

                for item in split_line:
                    if (item == 'A') or (item == 'X'):
                        formatted_round.append('rock')

                    elif (item == 'B') or (item == 'Y'):
                        formatted_round.append('paper')

                    elif (item == 'C') or (item == 'Z'):
                        formatted_round.append('scissors')

                """

                #rounds.append(formatted_round)

        return rounds

def process_round(round: list) -> int:
    """ Processes a round and determines number of points won """

    # Selected shape gives points
    # Rock -> 1 point
    # Paper -> 2 points
    # Scissors -> 3 points

    # Win -> 6 points
    # Lose -> 0 points
    # Draw -> 3 points

    """

    # part 1

    moves = {
            'rock': {
                'beats': 'scissors', 
                'loses': 'paper', 
                'points': 1, 
                },
            'paper': {
                'beats': 'rock', 
                'loses': 'scissors', 
                'points': 2, 
                },
            'scissors': {
                'beats': 'paper', 
                'loses': 'rock', 
                'points': 3, 
                }
            }

    opponent = round[0]
    player = round[1]

    if moves[player]['beats'] == opponent:

        return 6 + moves[player]['points']

    elif player == opponent:

        return 3 + moves[player]['points']

    elif moves[player]['beats'] != opponent:

        return moves[player]['points']

    """

    # Part 2

    moves = {
            'A': {'beats': 'C', 'loses': 'B', 'points': 1},
            'B': {'beats': 'A', 'loses': 'C', 'points': 2},
            'C': {'beats': 'B', 'loses': 'A', 'points': 3}
            }

    opponent = round[0]
    player = round[1]

    if player == 'X':
        losing_move = moves[opponent]['beats']

        return moves[losing_move]['points']

    elif player == 'Y':
        return 3 + moves[opponent]['points']

    elif player == 'Z':
        winning_move = moves[opponent]['loses']

        return 6 + moves[winning_move]['points']

rounds = load_rounds()

result = sum(list(map(process_round, rounds)))

print('Total score: ', result)
