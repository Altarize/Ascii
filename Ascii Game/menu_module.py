import cfg
import map_module

player = cfg.player


def menu_load():
    if player.rules:
        print("Game Rules")
        player.rules = False
        input("< ")
    else:
        print("1. New Game")
        print("2. Load Game")
        print("3. Rules")
        print("4. Quit")
        choice = input("> ")
        if choice == "1":
            player.name = input("> Enter Name: ")
            player.menu = False
            player.map_open = True
            player.max_hp = player._max_hp
            player.hp = player._hp
            player.atk = player._atk
            player.dfn = player._dfn
            player.gold = player._gold
            player.y = player._y
            player.x = player._x
            map_module.the_map.update()
        elif choice == "2":
            try:
                player.load_save()
            except OSError:
                print("No Save File!")
                input("<")
        elif choice == "3":
            player.rules = True
        elif choice == "4":
            quit()
        else:
            print("< Please enter a option number.")
