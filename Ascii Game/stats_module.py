import cfg
import map_module

player = cfg.player
the_map = map_module.the_map


def stats_load():
    cfg.draw()
    print(f"HEALTH: {player.hp}/{player.max_hp}  GOLD: {player.gold}")
    print(f"ATTACK: {player.atk} DEFENCE: {player.dfn}")
    cfg.draw()
    print(f"X: {player.x}")
    cfg.draw()

    choice: str = str(input(">").lower())

    if choice == "save":
        player.save()
        player.stats = False
        player.menu = True
    elif choice == "add":
        player.max_hp += 10
        player.hp += 10
        player.atk += 1
        player.dfn += 1
        player.gold += 100
        print("bonus stats")
    elif choice == "map":
        player.stats = False
        player.map_open = True
