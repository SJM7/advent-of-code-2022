class Monkey:

    def __init__ (self, starting_items, operation, test, if_true, if_false, index):
        self.starting_items = [int(item.replace(",", "")) for item in starting_items]
        self.scored_items = []

        self.operation = (operation[1], operation[2])
        self.test = test
        self.if_true = if_true
        self.if_false = if_false

        self.items_inspected = 0
        self.monkey_index = index
        self.monkies = None
    
    def _get_score(self, item: int) -> int:
        if self.operation[1] == "old":
            number = item
        else:
            number = int(self.operation[1])

        if self.operation[0] == "+":
            return item + number
        elif self.operation[0] == "-":
            return item - number
        elif self.operation[0] == "*":
            return item * number
        elif self.operation[0] == "/":
            if number == 0:
                return 0
            else:
                return item // number
    def _test_score(self, score: int):
        worry_level = score % 9699690
        if worry_level % self.test == 0:
            self.monkies[self.if_true].starting_items.append(worry_level)
        else:
            self.monkies[self.if_false].starting_items.append(worry_level)
    
    
    def score_items(self):
        items_thrown = []

        for item in self.starting_items:
            #score = self._get_score(item) // 3
            score = self._get_score(item)

            self._test_score(score)
            self.items_inspected += 1
            items_thrown.append(item)
            
        
        self.starting_items = [item for item in self.starting_items if item not in items_thrown]
    
    



    def monkey_state(self):
        print(f"Monkey {self.monkey_index}: {self.starting_items}")

            

def load_data():
    monkies = {}

    with open("input.txt") as file:
        current_monkey = None
        for line in file:
            formatted_line = line.strip()

            if formatted_line.startswith("Monkey"):
                current_monkey = formatted_line.split(" ")[1].replace(":", "")
                monkies[current_monkey] = {}

            elif "Starting items:" in formatted_line:
                monkies[current_monkey]["starting_items"] = formatted_line.split(" ")[2:]

            elif "Operation:" in formatted_line:
                monkies[current_monkey]["operation"] = formatted_line.split(" ")[3:]

            elif "Test:" in formatted_line:
                monkies[current_monkey]["test"] = int(formatted_line.split(" ")[3])
            
            elif "If true:" in formatted_line:
                monkies[current_monkey]["if_true"] = int(formatted_line.split(" ")[-1])

            elif "If false:" in formatted_line:
                monkies[current_monkey]["if_false"] = int(formatted_line.split(" ")[-1])

    return monkies

data = load_data()

monkeys = []

for index, monkey in data.items():
    monkey = Monkey(
        data[index]["starting_items"], 
        data[index]["operation"], 
        data[index]["test"], 
        data[index]["if_true"], 
        data[index]["if_false"], index
        )
    monkeys.append(monkey)

for monkey in monkeys:
    monkey.monkies = monkeys

for i in range(0, 10000):
    print(i)
    for monkey in monkeys:
        monkey.score_items()


for monkey in monkeys:
    print(f"Monkey {monkey.monkey_index} inspected items {monkey.items_inspected} times")