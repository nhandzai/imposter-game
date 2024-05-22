import crew
import random

colors = [
    "red",
    "blue",
    "green",
    "black",
    "white"
]


class GameManager:
    def __init__(self, n, m, max_liar):
        self.n = n
        self.m = m
        self.max_liar = max_liar
        self.color_range = []
        self.map_data = self.create_map()
    
       
    def checker(self,i,j):
        return self.map_data[i][j].is_lie
            
    def create_map(self):
        map_data = []
        names = [chr(65 + i) for i in range(self.n * self.m)]
        index = 0
        lies_positions = random.sample(range(self.n * self.m), self.max_liar)
        for i in range(self.n):
            row = []
            for j in range(self.m):
                color = random.choice(colors)
                if index in lies_positions:
                    row.append(
                        crew.Crew(names[index], (i, j), color, True))
                else:
                    row.append(
                        crew.Crew(names[index], (i, j), color))
                index += 1
            if color != self.color_range:
                self.color_range.append(color)
            map_data.append(row)

        return map_data

    def print_map(self):
        max_name_length = max(len(element.name)
                              for row in self.map_data for element in row)
        max_script_length = max(len(element.script) if not element.is_lie else len(
            '(isLie)') for row in self.map_data for element in row)

        for row in self.map_data:
            for element in row:
                if element.is_lie:
                    print(f'{element.name:<{max_name_length}} ({element.script})liar'.ljust(
                        max_name_length + max_script_length + 4), end='')
                else:
                    print(f'{element.name:<{max_name_length}} ({element.script})'.ljust(
                        max_name_length + max_script_length + 4), end='')
            print()


manager = GameManager(3, 3, 2)
for row in manager.map_data:
    for element in row:
        element.getScript(manager)
manager.print_map()
