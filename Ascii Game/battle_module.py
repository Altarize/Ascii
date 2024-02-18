import cfg
import random
import math


class Player:
    def __init__(self):
        self.is_alive = True
        self.block = 0
        self.card_draw = 3
        self.cards = {
            "Bolt": 3,
            "Def": 3,
            "Blast": 8
        }
        self.draw_pile = ["Bolt", "Bolt", "Bolt", "Def", "Def", "Def", "Blast"]
        self.disc_pile = []
        self.hand = []

    def reset(self):
        self.draw_pile = ["Bolt", "Bolt", "Bolt", "Def", "Def", "Def", "Blast"]
        self.disc_pile = []
        self.hand = []


class Enemy:
    def __init__(self, name, hp, dmg):
        self.is_alive = True
        self.name = name
        self.hp = hp
        self.max_hp = self.hp
        self.block = 0
        self.dmg = dmg

    def res(self):
        self.is_alive = True
        self.hp = self.max_hp


player = Player()
basic_monster = Enemy("basic monster", 45, 5)


def battle_start():
    if cfg.player.hp <= 0:
        cfg.player.hp = 0
        player.is_alive = False
    else:
        player_turn()


def player_turn():
    player.reset()
    random.shuffle(player.draw_pile)
    while player.is_alive and basic_monster.is_alive:
        player.block = 0
        if len(player.draw_pile) < player.card_draw:
            cards_left = player.card_draw - len(player.draw_pile)
            for i in player.draw_pile:
                player.hand.append(i)
            player.draw_pile = player.disc_pile
            player.disc_pile = []
            random.shuffle(player.draw_pile)

            while cards_left > 0:
                cards_left -= 1
                player.hand.append("".join(player.draw_pile[0:1]))
                player.draw_pile = player.draw_pile[1:]
        else:
            player.hand = player.draw_pile[0:player.card_draw]
            player.draw_pile = player.draw_pile[player.card_draw:]
        print(player.draw_pile)
        print(player.hand)
        print(player.disc_pile)
        player_choice()
    else:
        if player.is_alive:
            print("You win")
            cfg.player.battle = False
            cfg.player.map_open = True

        else:
            print("You lose")
            exit()


def player_choice() -> None:
    global pre_health_player, pre_health_monster
    card_choice = input("Choose a card to use\n> ").lower()
    pre_health_monster = basic_monster.hp
    if card_choice == 'blast':
        if 'Blast' in player.hand:
            basic_monster.hp -= player.cards['Blast'] + cfg.player.atk
        else:
            print("This card isn't in your hand")
    elif card_choice == 'bolt':
        if 'Bolt' in player.hand:
            basic_monster.hp -= player.cards['Bolt'] + cfg.player.atk
        else:
            print("This card isn't in your hand")
    elif card_choice == 'def':
        if 'Def' in player.hand:
            player.block += player.cards['Def'] + cfg.player.dfn
        else:
            print("This card isn't in your hand")
    pre_health_player = cfg.player.hp

    for i in player.hand:
        player.disc_pile.append(i)
    player.hand = []

    monster_atk()


def monster_atk() -> None:
    if basic_monster.hp <= 0:
        basic_monster.hp = 0
        basic_monster.is_alive = False
    else:
        if player.block == 0:
            cfg.player.hp -= basic_monster.dmg
        else:
            cfg.player.hp -= max(0, basic_monster.dmg - player.block)
    if cfg.player.hp <= 0:
        cfg.player.hp = 0
        player.is_alive = False

    health_bars()


def health_bars():
    player_bar = cfg.player.max_hp / 10
    enemy_bar = basic_monster.max_hp / 10
    print(f"Player HP: {cfg.player.hp}/{cfg.player.max_hp}")
    print(f'|{"X" * int(cfg.player.hp / player_bar)}{"_" * math.ceil((cfg.player.max_hp - cfg.player.hp) / player_bar)}|'
          f' -> You took {pre_health_player - cfg.player.hp} damage ')
    print("")
    print(f"Enemy HP: {basic_monster.hp}/{basic_monster.max_hp} -> You dealt {pre_health_monster - basic_monster.hp} damage")
    print(f'|{"X" * int(basic_monster.hp / enemy_bar)}{"_" * math.ceil((basic_monster.max_hp - basic_monster.hp) / enemy_bar)}|')
    input("<")

    player_turn()