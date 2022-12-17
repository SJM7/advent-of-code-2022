import pprint

def load_data() -> list:
    commands = []

    with open("test_case_part1.txt") as file:
        for line in file:
            formatted_line = line.strip().rstrip("\n").split(" ")
            
            if formatted_line[0] == "noop":
                commands.append((formatted_line[0], 0))
            else:
                commands.append((formatted_line[0], int(formatted_line[1])))

    return commands

def write_screen(monitor: list, register: int, cycles: int) -> list:

    lit_pixel = "#"

    current_position = (cycles % 40) - 1
    sprite_positions = [register - 1, register, register + 1]
    print(current_position, sprite_positions)

    if current_position in sprite_positions:
        if cycles in range(1, 40):
            monitor[0][current_position] = lit_pixel
        elif cycles in range(41, 80):
            monitor[1][current_position] = lit_pixel
        elif cycles in range(81, 120):
            monitor[2][current_position] = lit_pixel
        elif cycles in range(121, 160):
            monitor[3][current_position] = lit_pixel
        elif cycles in range(161, 200):
            monitor[4][current_position] = lit_pixel
        elif cycles in range(201, 240):
            monitor[5][current_position] = lit_pixel

    return monitor


def run_program(instructions: list):

    register = 1
    cycles = 1

    read_cycles = [20, 60, 100, 140, 180, 220]

    signal_strengths = []

    monitor = [
        [],
        [],
        [],
        [],
        [],
        []
    ]

    for line in monitor:
        for i in range(0, 40):
            line.append(".")
    print(len(monitor[0]))

    for instruction in instructions:
        command, value = instruction
        
        if command == "noop":
            #print(f"On cycle {cycles}, the register is {register}, signal strength is {cycles * register}")
            monitor = write_screen(monitor, register, cycles)
            cycles += 1
            if cycles in read_cycles: 
                signal_strengths.append(f"Cycles {cycles}: {register}")
        elif command == "addx":

            for i in range(2):
                if cycles in read_cycles:
                    signal_strengths.append(f"Cycles {cycles}: {register}, signal strength is {cycles * register}")
                monitor = write_screen(monitor, register, cycles)
                
                cycles += 1
            register += value

    print(monitor[0])
    print(monitor[1])
    print(monitor[2])
    print(monitor[3])
    print(monitor[4])
    print(monitor[5])

        

data = load_data()
run_program(data)
