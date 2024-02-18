import os
import map_module

the_map = map_module.the_map


class Player:
    run = True
    menu = True
    map_open = False
    stats = False
    battle = False
    rules = False

    def __init__(self) -> None:
        self.list_stats = list[str]
        self.name = ""
        self.max_hp, self._max_hp = 50, 50
        self.hp, self._hp = 50, 50
        self.atk, self._atk = 0, 0
        self.dfn, self._dfn = 0, 0
        self.gold, self._gold = 0, 0
        self.y, self._y = 0, 0
        self.x, self._x = 0, 0
        self.x_max = the_map.x_len - 1
        self.y_max = the_map.y_len - 1
        self.x_min = 0
        self.y_min = 0

    def save(self) -> None:
        self.list_stats = [
            self.name,
            str(self.max_hp),
            str(self.hp),
            str(self.atk),
            str(self.dfn),
            str(self.gold),
            str(self.y),
            str(self.x)]
        with open("GameSave", "w") as f:
            for item in self.list_stats:
                f.write(item + "\n")

    def load_save(self) -> None:
        with open("GameSave", "r") as f:
            load_list = f.readlines()
            if len(load_list) == 8:
                self.name = str(load_list[0][:-1])
                self.max_hp = int(load_list[1][:-1])
                self.hp = int(load_list[2][:-1])
                self.atk = int(load_list[3][:-1])
                self.dfn = int(load_list[4][:-1])
                self.gold = int(load_list[5][:-1])
                self.y = int(load_list[6][:-1])
                self.x = int(load_list[7][:-1])
                clear()
                print(f"< Welcome back {self.name}!")
                self.menu = False
                self.map_open = True
            else:
                print("< Corrupted save file!")
                input("< ")


player = Player()


def draw() -> None:
    # print("Oo.. _ ___oOo___ _ ..oO")
    print("----------------------")


def clear() -> None:
    os.system("cls")

