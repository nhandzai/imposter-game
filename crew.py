import random


scripts = [
    "Above me is ",
    "Below me is ",
    "To my left is ",
    "To my right is ",
    "Next to me is ",
    "The top row has ",
    "The bottom row has ",
    "The left-most column has ",
    "The right-most column has ",
    "Among the ",
    "Among the ",
]

coordinates = [
    [-1, 0], [1, 0], [0, -1], [0, 1]
]


class Crew:
    def __init__(self, name, pos, color="red", is_lie=False) -> None:
        self.name = name
        self.pos = pos
        self.is_lie = is_lie
        self.color = color
        self.name += "-" + color

    def checker(self, manager):
        if self.randomScriptIndex in [0, 1, 2, 3]:
            x, y = self.pos[0] + coordinates[self.randomScriptIndex][0], self.pos[1] + \
                coordinates[self.randomScriptIndex][1]
            if 0 <= x < manager.n and 0 <= y < manager.m:
                if manager.map_data[x][y].is_lie:
                    self.script += "a liar"
                else:
                    self.script += "not a liar"
            else:
                self.script += "OUT OF BOUNDS"

        elif self.randomScriptIndex == 4:
            x_l, y_l = self.pos[0] + coordinates[2][0], self.pos[1] + \
                coordinates[2][1]
            x_r, y_r = self.pos[0] + coordinates[3][0], self.pos[1] + \
                coordinates[3][1]
            is_lie_found = 0
            for (x, y) in [(x_l, y_l), (x_r, y_r)]:
                if 0 <= x < manager.n and 0 <= y < manager.m:
                    if manager.map_data[x][y].is_lie:
                        is_lie_found += 1
                        break
            if is_lie_found:
                self.script += "a liar"
            else:
                self.script += "not a liar"

        elif self.randomScriptIndex in [5, 6, 7, 8]:
            if self.randomScriptIndex in [5, 6]:
                row_index = 0 if self.randomScriptIndex == 5 else manager.n - 1
                iterable_range = range(manager.m)
            else:
                col_index = 0 if self.randomScriptIndex == 7 else manager.m - 1
                iterable_range = range(manager.n)

            is_lie_found = 0
            for index in iterable_range:
                if self.randomScriptIndex in [5, 6]:
                    if manager.map_data[row_index][index].is_lie:
                        is_lie_found += 1
                else:
                    if manager.map_data[index][col_index].is_lie:
                        is_lie_found += 1
            if self.is_lie:
                is_lie_found = 0 if is_lie_found else 1

            self.script += f'{is_lie_found} liar'

        else:
            color_choice = random.choice(manager.color_range)
            is_lie_found = sum(1 for i in range(manager.n) for j in range(
                manager.m) if manager.map_data[i][j].is_lie and manager.map_data[i][j].color == color_choice)

            if self.is_lie:
                is_lie_found = 0 if is_lie_found else 1

            self.script += f'{color_choice} has {is_lie_found} liar'

        if self.is_lie:
            if "not" in self.script:
                self.script = self.script.replace("not ", "", 1)
            else:
                index = self.script.find("a liar")
                if index != -1:
                    self.script = self.script[:index] + \
                        "not " + self.script[index:]

    def getScript(self, manager):
        while True:
            self.randomScriptIndex = random.randint(0, len(scripts)-1)
            if self.randomScriptIndex < 4:
                x, y = self.pos[0] + coordinates[self.randomScriptIndex][0], self.pos[1] + \
                    coordinates[self.randomScriptIndex][1]
                if 0 <= x < manager.n and 0 <= y < manager.m:
                    break
            else:
                break
        self.script = scripts[self.randomScriptIndex]
        self.checker(manager)
