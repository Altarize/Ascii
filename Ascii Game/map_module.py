import battle_module
import cfg


class Map:
    def __init__(self) -> None:  # Creates a Map object, with 6 attributes and 2 methods.
        self.x_len: int = 20  # Map columns
        self.y_len: int = 1  # Map rows
        self.left: int = 0  # Empty dots left of "C" (increase to go right, decrease to go left)
        self.right: int = self.x_len - 1  # Empty dots right of "C" (decrease to go right, increase to go left)
        self.up: int = 0  # Empty lines above "C" (increase to go down, decrease to go up)
        self.down: int = self.y_len - 1  # Empty lines under the "C" (decrease to go down, increase to go up)

    def update(self) -> None:  # Updates the map objects values to match players x & y
        self.left = cfg.player.x  # Updates the left side according to player cord value
        self.right = (self.x_len - 1) - cfg.player.x  # Updates the right side to (map length - 1) - player cord
        self.up = cfg.player.y
        self.down = (self.y_len - 1) - cfg.player.y

    def render(self) -> None:  #
        print("X" + "-" * self.x_len + "X")  # Top border of map
        for i in range(self.up):  # Empty lines above player
            print("|" + "." * self.x_len + "|")  # Print empty lines with side border
        print("|" + "." * self.left + "C" + "." * self.right + "|")  # Player line empty with adaptive sides
        for i in range(self.down):  # Empty lines below player
            print("|" + "." * self.x_len + "|")  # Print empty lines with side border
        print("X" + "-" * self.x_len + "X")  # Bottom border of map


the_map = Map()


def map_load():
    the_map.update()
    the_map.render()
    choice = input(">").lower()
    if choice == "stats":
        cfg.player.map_open = False
        cfg.player.stats = True
    if choice == "":
        cfg.player.x += 1
        the_map.update()
        cfg.player.map_open = False
        cfg.player.battle = True

        # reward

