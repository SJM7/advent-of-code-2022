def load_data() -> str:
    with open("problem6.txt", "r") as file:
        data = file.read()

    return data

def parse_marker(signal: str):
    start_index = 0
    
    for i in range(0, len(signal) - 1):
        chunk = signal[i:i+14] # Change to 4 for part 1

        if len(chunk) != len(set(chunk)):
            next
        else:
            start_index = i + 14 # Change to 4 for part 1
            break

    print("Start index: ", start_index)
                       
data = load_data()
parse_marker(data)
