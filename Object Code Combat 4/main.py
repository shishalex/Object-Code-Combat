from player import Player
from weapon import Weapon
from potion import Potion


def main():
    p1 = Player("Marco Farina", 100, 15, 8)
    p2 = Player()

    print("=== SIMULAZIONE COMBATTIMENTO ===")

    print(p1)
    print(p2)
    print(" ")

    try:   
        weapon1 = Weapon("Spada Lunga", 5, 12, "melee")
    except Exception as e:
        print(f"Errore sconosciuto nella creazione dell'arma per {p1.name}: {str(e)}")
        weapon1 = Weapon("Spada Lunga", 5, 12, "melee")
    try:
        weapon2 = Weapon("Balestra pesante", 4, 12, "Ranged")
    except Exception as e:
        print(f"Errore sconosciuto nella creazione dell'arma per {p2.name}: {str(e)}")
        weapon2 = Weapon("Balestra pesante", 4, 12, "Ranged")

    setup_potions(p1)
    setup_potions(p2)

    try:
        p1.weapon = weapon1
    except TypeError as e:
        print(f"Errore nell'equipaggiare l'arma per {p1.name}: {str(e)}")
    try:
        p2.weapon = weapon2
    except TypeError as e:
        print(f"Errore nell'equipaggiare l'arma per {p2.name}: {str(e)}")

    weapon_equip(p1.name, weapon1)
    weapon_equip(p2.name, weapon2)
    print(" ")

    print("=== INIZIO COMBATTIMENTO ===")
    turns = 0
    while p1.is_alive() and p2.is_alive():
        turns += 1
        print(f"--- Turno {turns} ---")
        try:
            potion = p1.should_use_potion()
        except ValueError as e:
            print(f"{p1.name} tenta usare {potion}, ma si verifica un errore: {str(e)}")
        except TypeError as e:
            print(f"{p1.name} tenta usare {potion}, ma si verifica un errore: {str(e)}")
        except Exception as e:
            print(f"{p1.name} tenta usare {potion}, ma si verifica un errore: {str(e)}")
        if potion is not None:
            print(f"{p1.name} usa {potion}")

        try:
            damage1 = p1.attack(p2)
        except ValueError as e:
            print(f"Errore durante l'attacco di {p1.name}: {str(e)}")
            damage1 = 0
        except TypeError as e:
            print(f"Errore durante l'attacco di {p1.name}: {str(e)}")
            damage1 = 0
        except Exception as e:
            print(f"Errore durante l'attacco di {p1.name}: {str(e)}")
            damage1 = 0
        action(p1, p2, damage1)
        
        if not p2.is_alive():
            break

        try:
            potion = p2.should_use_potion()
        except ValueError as e:
            print(f"{p2.name} tenta usare {potion}, ma si verifica un errore: {str(e)}")
        except TypeError as e:
            print(f"{p2.name} tenta usare {potion}, ma si verifica un errore: {str(e)}")
        except Exception as e:
            print(f"{p2.name} tenta usare {potion}, ma si verifica un errore: {str(e)}")
        if potion is not None:
            print(f"{p2.name} usa {potion}")

        try:
            damage2 = p2.attack(p1)
        except ValueError as e:
            print(f"Errore durante l'attacco di {p2.name}: {str(e)}")
            damage2 = 0
        except TypeError as e:
            print(f"Errore durante l'attacco di {p2.name}: {str(e)}")
            damage2 = 0
        except Exception as e:
            print(f"Errore durante l'attacco di {p2.name}: {str(e)}")
            damage2 = 0
        action(p2, p1, damage2)

        p1.tick_buffs()
        p2.tick_buffs()

    print("=== FINE COMBATTIMENTO ===")
    try:
        p1_alive = p1.is_alive()
    except Exception as e:
        print(f"Errore nel controllo dello stato di {p1.name}: {str(e)}")
        p1_alive = False
    try:
        p2_alive = p2.is_alive()
    except Exception as e:
        print(f"Errore nel controllo dello stato di {p2.name}: {str(e)}")
        p2_alive = False

    if p1_alive and not p2_alive:
        victory(p1)
    elif p2_alive and not p1_alive:
        victory(p2)
    else:
        print("Il combattimento termina in pareggio!")

def weapon_equip(name: str, weapon: "Weapon"):
    print(f"{name} equipaggia: {weapon}")


def action(attacker: "Player", defender: "Player", damage):
    print(f"{attacker.name} attacca {defender.name} e infligge {damage} danni!")
    print(f"{defender.name} (HP:{defender.health}/{defender.max_health})\n")


def victory(player: "Player"):
    print(f"{player.name} vince il combattimento! {player.name} (HP:{player.health}/"
          f"{player.max_health})")


def setup_potions(player: Player) -> None:
    player.potions.append(Potion("Healing Draught", "heal", 10, 0))
    player.potions.append(Potion("Healing Draught", "heal", 10, 0))

    if player.strength >= player.dexterity:
        player.potions.append(Potion("Ogre Tonic", "buff_str", 2, 3))
    else:
        player.potions.append(Potion("Cat's Grace", "buff_dex", 2, 3))


if __name__ == "__main__":
    main()