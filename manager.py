import crew
import random

class GameManager:
    def __init__(self, n, m, k):
        self.n = n
        self.m = m
        self.k = k
        self.map_data = self.create_map()

    def create_map(self):
        map_data = []
        names = [chr(65 + i) for i in range(self.n * self.m)]
        index = 0
        lies_positions = random.sample(range(self.n * self.m), self.k)
        for i in range(self.n):
            row = []
            for j in range(self.m):
                if index in lies_positions:
                    row.append(crew.Crew(names[index], (i, j), self.n, self.m, True))
                else:
                    row.append(crew.Crew(names[index], (i, j), self.n, self.m))
                index += 1
            map_data.append(row)

        return map_data

    def print_map(self):
        for row in self.map_data:
            for element in row:
                if element.isLie:
                    print('isLie=True', end='\t')
                else:
                    print(f'{element.name}({element.script})', end='\t')
            print()


manager = GameManager(3, 3, 1)
for row in manager.map_data:
    for element in row:
        element.getScript(manager.map_data)
manager.print_map()
