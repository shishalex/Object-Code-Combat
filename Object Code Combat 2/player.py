from random import randint
from random import choice
from weapon import Weapon


class Player:
    names = ["Aric", "Elara", "Torvin", "Lyra", "Kael", "Seraphina", "Drakon", "Isolde", "Aldric", "Morwen"]
    surnames = ["Spadaombra", "Chiarafoglia", "Ferroscuro", "Ventogelido", "Pietradura", "Aliargento", "Cuorleale",
                "Silenzioso", "Neromante", "Stellardente"]

    def __init__(self, name: str = choice(names) + " " + choice(surnames),  max_health: int = randint(90, 120), strength: int = randint(1, 20), dexterity: int = randint(1, 20)):
        self.__name: str = name

        self.__max_health: int = max_health
        if self.get_max_health() < 1:
            self.set_max_health(1)

        self.__health: int = self.get_max_health()

        self.__strength: int = strength
        if self.get_strength() > 20:
            self.set_strength(20)
        if self.get_strength() < 1:
            self.set_strength(1)

        self.__dexterity: int = dexterity
        if self.get_dexterity() > 20:
            self.set_dexterity(20)
        if self.get_dexterity() < 1:
            self.set_dexterity(1)

        self.__weapon: "Weapon" = None

    def equip(self, weapon: Weapon) -> None:
        self.__weapon = weapon

    def modifier(self) -> int:
        if self.get_weapon().get_type() == "melee":
            value = self.get_strength()
        else:
            value = self.get_dexterity()
        return (value - 10) // 2

    def is_alive(self) -> bool:
        if self.get_health() <= 0:
            return False
        else:
            return True

    def take(self, damage: int) -> int:
        self.set_health(self.get_health() - damage)
        if self.get_health() < 0:
            self.set_health(0)
        return damage

    def attack(self, enemy: "Player"):
        if self.get_weapon() == None:
            basic_damage = 1
        else:
            basic_damage = self.get_weapon().get_damage()
        damage = basic_damage + self.modifier()
        if damage < 0:
            damage = 0
        damage = enemy.take(damage)
        return damage

    def __str__(self):
        return (f"[{self.get_name()}] \nForza: {self.get_strength()}\nDestrezza: {self.get_dexterity()}\n"
                f"HP massimi: {self.get_max_health()}\nHP attuali: {self.get_health()}")

    def get_name(self) -> str:
        return self.__name

    def get_max_health(self) -> int:
        return self.__max_health

    def set_max_health(self, max_health: int) -> None:
        self.__max_health = max_health

    def get_health(self) -> int:
        return self.__health

    def set_health(self, health: int) -> None:
        self.__health = health

    def get_strength(self) -> int:
        return self.__strength

    def set_strength(self, strength: int) -> None:
        self.__strength = strength

    def get_dexterity(self) -> int:
        return self.__dexterity

    def set_dexterity(self, dexterity: int) -> None:
        self.__dexterity = dexterity

    def get_weapon(self) -> Weapon:
        return self.__weapon

    def equip(self, weapon: Weapon) -> None:
        self.__weapon = weapon
