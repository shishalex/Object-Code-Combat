from player import Player
from weapon import Weapon


def main():
    p1 = Player("Marco Farina", 100, 15, 8)
    p2 = Player()

    print("=== SIMULAZIONE COMBATTIMENTO ===")

    print(p1)
    print(p2)
    print(" ")
        
    weapon1 = Weapon("Spada Lunga", 5, 12, "melee")
    weapon2 = Weapon("Balestra pesante", 4, 12, "Ranged")

    p1.equip(weapon1)
    p2.equip(weapon2)

    weapon_equip(p1.get_name(), weapon1)
    weapon_equip(p2.get_name(), weapon2)
    print(" ")

    print("=== INIZIO COMBATTIMENTO ===")
    turns = 0
    while p1.get_health() > 0 and p2.get_health() > 0:
        turns += 1
        print(f"--- Turno {turns} ---")
        damage1 = p1.attack(p2)
        action(p1, p2, damage1)
        if p2.is_alive() == False:
            break
        damage2 = p2.attack(p1)
        action(p2, p1, damage2)

    print("=== FINE COMBATTIMENTO ===")
    if p1.is_alive():
        victory(p1)
    elif p2.is_alive():
        victory(p2)


def weapon_equip(name: str, weapon: "Weapon"):
    print(f"{name} equipaggia: {weapon}")


def action(attacker: "Player", defender: "Player", damage):
    print(f"{attacker.get_name()} attacca {defender.get_name()} e infligge {damage} danni!")
    print(f"{defender.get_name()} (HP:{defender.get_health()}/{defender.get_max_health()})\n")


def victory(player: "Player"):
    print(f"{player.get_name()} vince il combattimento! {player.get_name()} (HP:{player.get_health()}/"
          f"{player.get_max_health()})")


if __name__ == "__main__":
    main()