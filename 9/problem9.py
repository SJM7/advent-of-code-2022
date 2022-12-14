import math

def load_data() -> list:
    moves = []

    with open("problem9.txt", "r") as file:
        for line in file:
            formatted_line = line.rstrip("\n").split(" ")

            moves.append({"direction": formatted_line[0], "distance": int(formatted_line[1])})
    
    return moves
"""
# Part 1

def move_rope(moves: list):
    visited = set()

    head = (0, 0)
    tail = (0, 0)

    visited.add(tail)

    print(head, tail)

    for move in moves:
        direction = move["direction"]
        distance = move["distance"]

        for _ in range(distance):
            if direction == "U":
                head = (head[0], head[1] + 1)
            elif direction == "D":
                head = (head[0], head[1] - 1)
            elif direction == "R":
                head = (head[0] + 1, head[1])
            elif direction == "L":
                head = (head[0] - 1, head[1])

            point_distance = (abs(head[0] - tail[0]),abs(head[1] - tail[1]))

            not_touching = (abs(point_distance[0]) > 1) or (abs(point_distance[1]) > 1)

            signs = (
                int(math.copysign(1, head[0] - tail[0])), 
                int(math.copysign(1, head[1] - tail[1]))
                )

            if not_touching:
                if point_distance[0] == 2 and point_distance[1] == 0:
                    tail = (tail[0] + signs[0], tail[1])
                    visited.add(tail)
                elif point_distance[0] == 0 and point_distance[1] == 2:
                    tail = (tail[0], tail[1] + signs[1])
                    visited.add(tail)
                elif abs(head[0] - tail[0]) != abs(head[1] - tail[1]):
                    tail = (tail[0] + signs[0], tail[1] + signs[1])
                    visited.add(tail)
                    
    print("Unique positions visited: ", len(visited))
"""

# Part 2

def move_rope(moves: list):

    visited = set()

    visited.add((0,0))

    knots = []

    for i in range(10): 
        knots.append((0,0))

    for move in moves:
        direction = move["direction"]
        distance = move["distance"]

        for _ in range(distance):
            if direction == "U":
                knots[0] = (knots[0][0], knots[0][1] + 1)
            elif direction == "D":
                knots[0] = (knots[0][0], knots[0][1] - 1)
            elif direction == "R":
                knots[0] = (knots[0][0] + 1, knots[0][1])
            elif direction == "L":
                knots[0] = (knots[0][0] - 1, knots[0][1])
        
            for i in range(0, len(knots) - 1):
                head = knots[i]
                new_tail = knots[i + 1]
                #print(new_tail)
                
                point_distance = (abs(head[0] - new_tail[0]), abs(head[1] - new_tail[1]))

                not_touching = (abs(point_distance[0]) > 1) or (abs(point_distance[1]) > 1)

                signs = (
                    int(math.copysign(1, head[0] - new_tail[0])), 
                    int(math.copysign(1, head[1] - new_tail[1]))
                    )
                    
                if not_touching:
                    if point_distance[0] == 2 and point_distance[1] == 0:
                        new_tail = (new_tail[0] + signs[0], new_tail[1])
                    elif point_distance[0] == 0 and point_distance[1] == 2:
                        new_tail = (new_tail[0], new_tail[1] + signs[1])
                    elif abs(head[0] - new_tail[0]) + abs(head[1] - new_tail[1]) > 2:
                        new_tail = (new_tail[0] + signs[0], new_tail[1] + signs[1])

                knots[i + 1] = new_tail
                visited.add(knots[-1])

    print(len(visited))

data = load_data()
move_rope(data)