from player import Player
from weapon import Weapon

def main():
    if __name__ == "__main__":
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

        weapon_equip(p1.name, weapon1)
        weapon_equip(p2.name, weapon2)
        print(" ")

        print("=== INIZIO COMBATTIMENTO ===")
        turns = 0
        while p1.health > 0 or p2.health > 0:
            turns += 1
            print(f"--- Turno {turns} ---")
            damage1 = p1.attack(p2)
            action(p1, p2, damage1)
            damage2 = p2.attack(p1)
            action(p2, p1, damage2)

        print("=== FINE COMBATTIMENTO ===")
        if p1.is_alive() == True:
            victory(p1)
        elif p2.is_alive() == True:
            victory(p2)
            

def weapon_equip(name: str, weapon: "Weapon"):
    print(f"{name} equipaggia: {weapon}")

def action(attacker: "Player", defender: "Player", damage):
    print(f"{attacker.name} attacca {defender.name} e infligge {damage} danni!")
    print(f"{defender.name} (HP:{defender.health}/{defender.max_health})\n")

def victory(player: "Player"):
    print(f"{player.name} vince il combattimento! {player.name} (HP:{player.health}/{player.max_health})")

main()