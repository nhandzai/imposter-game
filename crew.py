import random

sus = "SUS"
notSus = "not SUS"
scripts = [
    "Above me is ",
    "Below me is ",
    "To my left is ",
    "To my right is ",
    "Next to me is ",
    "The top row has at least ",
    "The bottom row has at least ",
    "The left-most column has at least ",
    "The right-most column has at least ",
]

coordinates = [
    [-1, 0], [1, 0], [0, -1], [0, 1]
]


class Crew:
    def __init__(self, name, pos, n, m, isLie=False) -> None:
        self.name = name
        self.pos = pos
        self.n = n
        self.m = m
        self.isLie = isLie

    def checker(self, map_data):
        if self.randomScriptIndex in [0, 1, 2, 3]:
            x, y = self.pos[0] + coordinates[self.randomScriptIndex][0], self.pos[1] + \
                coordinates[self.randomScriptIndex][1]
            if 0 <= x < self.n and 0 <= y < self.m:
                if map_data[x][y].isLie:
                    self.script += sus
                else:
                    self.script += notSus
            else:
                self.script += "OUT OF BOUNDS"
        elif self.randomScriptIndex in [5, 6]:
            row_index = 0 if self.randomScriptIndex == 5 else self.n-1
            for j in range(self.m):
                if map_data[row_index][j].isLie:
                    self.script += "1 " + sus
                    return
            self.script += "0 " + sus
        elif self.randomScriptIndex in [7, 8]:
            col_index = 0 if self.randomScriptIndex == 7 else self.m-1
            for i in range(self.n):
                if map_data[i][col_index].isLie:
                    self.script += "1" + sus
                    return
            self.script += "0 " + sus

    def getScript(self, map_data):
        while True:
            self.randomScriptIndex = random.randint(0, len(scripts)-1)
            if self.randomScriptIndex < 4:
                x, y = self.pos[0] + coordinates[self.randomScriptIndex][0], self.pos[1] + \
                    coordinates[self.randomScriptIndex][1]
                if 0 <= x < self.n and 0 <= y < self.m:
                    break
            else:
                break
        self.script = scripts[self.randomScriptIndex]
        self.checker(map_data)
