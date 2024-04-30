import random

sus = "SUS"
notSus = "not SUS"
scripts = [
    "Above me is ",
    "Below me is ",
    "To my left is",
    "To my right is",
    "Next to me is ",
    "The top row has at least ",
    "The bottom row has at least ",
    "The right-most column has at least ",
    "The left-most column has at least ",
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

    def checker(self,map_data):
        if self.randomScriptIndex in [0, 1, 2, 3]:
            if not map_data[coordinates[self.randomScriptIndex]].isLie:
                self.script += sus
            else:
                self.script += notSus
        elif self.randomScriptIndex == 5 or self.randomScriptIndex == 6:
            row_index = 0 if self.randomScriptIndex == 5 else -1
            for j in range(self.m):
                if not map_data[row_index][j].isLie:
                    self.script += "1" + sus
                else:
                    self.script += "0" + sus

    def getScript(self,map_data):
        self.randomScriptIndex = random.randint(6, len(scripts)-1)
        self.script = scripts[self.randomScriptIndex]
        self.checker(map_data)
