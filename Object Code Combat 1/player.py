from random import randint
from random import choice
from weapon import Weapon

class Player:
    names = ["Aric", "Elara", "Torvin", "Lyra", "Kael", "Seraphina", "Drakon", "Isolde", "Aldric", "Morwen"]
    surnames = ["Spadaombra", "Chiarafoglia", "Ferroscuro", "Ventogelido", "Pietradura", "Aliargento", "Cuorleale",
                "Silenzioso", "Neromante", "Stellardente"]

    def __init__(self, name: str= choice(names) + choice(surnames),  max_health: int= randint(90, 120), strength: int= randint(1, 20), dexterity: int =randint(1, 20)):
        self.name: str = name
        self.max_health: int = max_health
        if self.max_health < 1:
            self.max_health = 1
        self.health: int = self.max_health
        self.strength: int = strength
        if self.strength > 20:
            self.strength = 20
        if self.strength < 1:
            self.strength = 1
        self.dexterity: int = dexterity
        if self.dexterity > 20:
            self.dexterity = 20
        if self.dexterity < 1:
            self.dexterity = 1
        self.weapon: "Weapon" = None

    def equip(self) -> None:
        self.weapon = Weapon(self.strength, self.dexterity)

    def modifier(self) -> int:
        if self.weapon.type == "Melee":
            value = self.strength
        elif self.weapon.type == "Ranged":
            value = self.dexterity
        return (value - 10) // 2

    def is_alive(self) -> bool:
        if self.health <= 0:
            return False
        else:
            return True

    def take(self, damage: int) -> int:
        self.health -= damage
        if self.health < 0:
            damage += self.health
            self.health = 0
        return damage

    def attack(self, enemy: "Player"):
        if self.weapon == None:
            basic_damage = 1
        else:
            basic_damage = self.weapon.get_damage()
        damage = basic_damage + self.modifier()
        if damage < 0:
            damage = 0
        enemy.take(damage)

    def __str__(self):
        return f"[{self.name}] \nHP massimi: {self.max_health}\nHP attuali: {self.health}"