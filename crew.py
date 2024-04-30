import random
import manager
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
    def __init__(self, name, pos, isLie=False) -> None:
        self.name = name
        self.pos = pos
        self.isLie = isLie
        self.randomScriptIndex = random.randint(0, len(scripts)-1)
        self.script = scripts[self.randomScriptIndex]
        self.checker()

    def checker(self, manager:'manager'):
        if self.randomScriptIndex in [0, 1, 2, 3]:
            if not manager.map_data[coordinates[self.randomScriptIndex]].isLie:
                self.script += sus
            else:
                self.script += notSus
        if self.randomScriptIndex == 5:
            for j in range(0, len(manager.map_data[0])):
                if not manager.map_data[0][j].isLie:
                    self.script += "1" + sus
                else:
                    self.script += "0" + sus
        if self.randomScriptIndex == 6:
            for j in range(len[manager.map_data]-1, len(manager.map_data[0])):
                if not manager.map_data[0][j].isLie:
                    self.script += "1" + sus
                else:
                    self.script += "0" + sus
