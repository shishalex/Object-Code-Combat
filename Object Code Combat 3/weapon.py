from random import randint

class Weapon:
    __allowed_types = {"ranged", "melee"}

    def __init__(self, name:str, min_damage:int, max_damage:int, types:str):
        self.__name = name
        self.__min_damage = min_damage
        self.__max_damage = max_damage
        self.__types = types.lower

    def get_damage(self) -> int:
        return randint(self.min_damage, self.max_damage)
    
    def __str__(self):
        return f"{self.name} ({self.min_damage}-{self.max_damage} dmg)"

    @property
    def name(self) -> str:
        return self.__name

    @property
    def min_damage(self) -> int:
        return self.__min_damage

    @min_damage.setter
    def min_damage(self, new_min_damage: int):
        if new_min_damage < 1:
            print("Il valore del danno minimo è troppo piccolo! "
                  "È stato impostato automaticamente ad 1.")
            self.__min_damage = 1

        self.__min_damage = new_min_damage

    @property
    def max_damage(self) -> int:
        return self.__max_damage

    @max_damage.setter
    def max_damage(self, new_max_damage: int):
        if new_max_damage < self.min_damage:
            print("Il valore del danno massimo è più piccolo del danno minimo! "
                  f"È stato impostato automaticamente ad {self.min_damage}.")
            self.__max_damage = self.min_damage

        self.__min_damage = new_max_damage
    @property
    def types(self):
        return self.__types

    @types.setter
    def types(self, new_type):
        if new_type not in Weapon.__allowed_types:
            print(
                f"Valore non valido per 'effect': '{new_type}'. "
                f"I valori ammessi sono: {', '.join(Weapon.__allowed_types)}"
            )
            return
