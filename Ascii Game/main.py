import cfg
import menu_module
import map_module
import stats_module
import battle_module

player = cfg.player

while player.run:
    while player.menu:
        menu_module.menu_load()
    while player.map_open:
        map_module.map_load()
    while player.stats:
        stats_module.stats_load()
    while player.battle:
        battle_module.battle_start()
        #battle_module.basic_monster.res()