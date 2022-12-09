class Node(object):
    def __init__(self, name: str, parent: str):
        self.name = name
        self.parent = parent
        self.children = []
        self.data = []

    def add_child(self, child: str):
        self.children.append(child)

    def add_data(self, data: str):
        self.data.append(data)

    def __repr__(self):
        return f"Node({self.name}, {self.parent})"

def load_data() -> list:
    command_output = []

    with open("problem7.txt", "r") as file:
        for line in file:
            if line.startswith("$"):
                command_output.append(line.removeprefix("$").strip("\n").lstrip(" "))

            else:
                command_output.append(line.strip("\n"))
    
    return command_output

def parse_data(data: list) -> Node:
    root = Node("/", None)

    current_node = root

    for line in data:
        if line.startswith("cd") and line != "cd ..":
            folder_name = line.split(" ")[1]

            for folder in current_node.children:
                if folder.name == folder_name:
                    current_node = folder
                    break
        
        elif line == "cd ..":
            current_node = current_node.parent

        elif line.startswith("dir"):
            folder_name = line.split(" ")[1]

            child_node = Node(folder_name, current_node)
            current_node.add_child(child_node)

        elif line != "ls":
            file_size = int(line.split(" ")[0])

            current_node.add_data(file_size)

    return root

def traverse_tree(tree: Node):
    total = 0

    for child in tree.children:
        print("Directory: ", child.name, "Parent: ", child.parent.name, "Files: ", child.data)

        traverse_tree(child)

"""
# Part 1
directories = []

def sum_directories(tree: Node):
    total = 0
    
    total += sum(tree.data)

    for child in tree.children:
        total += sum_directories(child)

    #if total < 100000:
        directories.append(total)

    return total
"""

# Part 2

directories = []

def total_size(tree: Node) -> int:
    total = 0

    total += sum(tree.data)

    for child in tree.children:
        total += total_size(child)

    return total

def delete_directories(tree: Node, size: int) -> int:
    total_space = 70000000
    unused_space = total_space - size
    space_needed = 30000000 - unused_space

    total = 0

    total += sum(tree.data)

    for child in tree.children:
        total += delete_directories(child, size)

    if total >= space_needed:
        directories.append(total)

    return total

data = load_data()
tree = parse_data(data)   

size = total_size(tree)

delete_directories(tree, size)
print(directories)
print("Directory to delete: ", min(directories))

# Use below for part 1

#print(directories)
#print("Total size of all files: ", sum(directories))