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
        self.__health: int = self.max_health
        self.__strength: int = strength
        self.__dexterity: int = dexterity
        self.__weapon: "Weapon" = None

    def equip(self, weapon: Weapon) -> None:
        self.__weapon = weapon

    def modifier(self) -> int:
        if self.weapon.types == "melee":
            value = self.strength
        else:
            value = self.dexterity
        return (value - 10) // 2

    def is_alive(self) -> bool:
        if self.health <= 0:
            return False
        else:
            return True

    def take(self, damage: int) -> int:
        self.health = self.health - damage
        if self.health < 0:
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
        damage = enemy.take(damage)
        return damage

    def heal(self, amount: int) -> None:
        self.health += amount

    def add_buff(self, stat: str, amount: int, duration: int) -> None:
        return

    def __str__(self):
        return (f"[{self.name}] \nForza: {self.strength}\nDestrezza: {self.dexterity}\n"
                f"HP massimi: {self.max_health}\nHP attuali: {self.health}")

    @property
    def name(self) -> str:
        return self.__name

    @property
    def max_health(self) -> int:
        return self.__max_health

    @max_health.setter
    def max_health(self, new_max_health: int) -> None:
        if new_max_health < 1:
            print("Il valore della vita inserito è troppo piccolo!")
            self.max_health = 1
            return
        self.__max_health = new_max_health

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, new_health: int) -> None:
        self.__health = new_health

    @property
    def strength(self) -> int:
        return self.__strength

    @strength.setter
    def strength(self, new_strength: int) -> None:
        if new_strength > 20:
            self.strength = 20
            print("Hai inserito un valore di forza più alto di 20!"
                  "La forza è stata impostata al suo massimo.")
            return

        if new_strength < 1:
            self.strength = 1
            print("Hai inserito un valore di forza più basso di 1!"
                  "La forza è stata impostata al suo minimo.")
            return

        self.__strength = new_strength

    @property
    def dexterity(self) -> int:
        return self.__dexterity

    @dexterity.setter
    def dexterity(self, new_dexterity: int) -> None:
        if new_dexterity > 20:
            self.dexterity = 20
            print("Hai inserito un valore di destrezza più alto di 20!"
                  "La destrezza è stata impostata al suo massimo.")
            return

        if new_dexterity < 1:
            self.dexterity = 1
            print("Hai inserito un valore di destrezza più basso di 1!"
                  "La destrezza è stata impostata al suo minimo.")
            return

        self.__dexterity = new_dexterity

        self.__dexterity = new_dexterity

    @property
    def weapon(self) -> Weapon:
        return self.__weapon

    def equip(self, weapon: Weapon) -> None:
        self.__weapon = weapon
