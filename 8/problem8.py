from functools import reduce

def load_data() -> list:
    tree_matrix = []

    with open("problem8.txt", "r") as file:
        for line in file:
            formatted_line = line.rstrip("\n")
            trees = []

            for char in formatted_line:
                trees.append(int(char))
            
            tree_matrix.append(trees)

    return tree_matrix

def search_trees(tree_matrix: list, x: int, y: int, direction: str) -> list:
    if direction == "up":
        return [tree_matrix[i][x] for i in range(y - 1, -1, -1)]
    elif direction == "down":
        return [tree_matrix[i][x] for i in range(y + 1, len(tree_matrix))]
    elif direction == "left":
        return [tree_matrix[y][i] for i in range(x - 1, -1, -1)]
    elif direction == "right":
        return [tree_matrix[y][i] for i in range(x + 1, len(tree_matrix[y]))]

# Part 1

def validate_searches(searches: list, tree_value: int) -> bool:
    for search in searches:
        if search >= tree_value:
            return False

    return True

def find_visible_trees(tree_matrix: list) -> int:
    trees_visible = 0

    for i in range(len(tree_matrix)):
        for j in range(len(tree_matrix[i])):
            if j == 0 or j == len(tree_matrix[i]) - 1 or i == 0 or i == len(tree_matrix) - 1:
                trees_visible += 1

            else:
                current_tree = tree_matrix[i][j]

                search_directions = [
                    search_trees(tree_matrix, j, i, "up"), 
                    search_trees(tree_matrix, j, i, "down"), 
                    search_trees(tree_matrix, j, i, "left"), 
                    search_trees(tree_matrix, j, i, "right")
                    ]

                for search in search_directions:
                    if validate_searches(search, current_tree):
                        trees_visible += 1
                        break
    print("Trees visible: ", trees_visible)

# Part 2

def get_score(searches: list, tree_value: int) -> int:
    score = 0

    for i in range(0, len(searches)):
        if searches[i] >= tree_value:
            score += i + 1
            break
    
    if score == 0:
        score += len(searches)

    return score

def score_trees(tree_matrix: list):
    total_scores = []

    for i in range(len(tree_matrix)):
        for j in range(len(tree_matrix[i])):
            current_tree = tree_matrix[i][j]
            
            search_directions = [
                {"up": search_trees(tree_matrix, j, i, "up")}, 
                {"down": search_trees(tree_matrix, j, i, "down")}, 
                {"left": search_trees(tree_matrix, j, i, "left")}, 
                {"right": search_trees(tree_matrix, j, i, "right")}
                ]

            scores = []

            for search in search_directions:
                for key, value in search.items():
                    scores.append(get_score(value, current_tree))
            
            print("Position: ", i, j)
            print("Value: ", current_tree)
            print("Searches: ", search_directions)
            print("Scores: ", scores)
            print("Total: ", reduce(lambda x, y: x * y, scores))
            print("\n")


            total_scores.append(reduce(lambda x, y: x * y, scores))

    print("Total scores: ", total_scores)
    print("Maximum score: ", max(total_scores))

tree_matrix = load_data()
#find_visible_trees(tree_matrix)
score_trees(tree_matrix)