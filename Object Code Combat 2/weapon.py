from random import randint


class Weapon:
    def __init__(self, name:str, min_damage:int, max_damage:int, types:str):
        self.__name = name
        self.__min_damage = min_damage
        self.__max_damage = max_damage
        self.__types = types.lower

    def get_damage(self) -> int:
        return randint(self.get_min_damage(), self.get_max_damage())
    
    def __str__(self):
        return f"{self.get_name()} ({self.get_min_damage()}-{self.get_max_damage()} dmg)"

    def get_name(self) -> str:
        return self.__name

    def get_min_damage(self) -> int:
        return self.__min_damage

    def get_max_damage(self) -> int:
        return self.__max_damage

    def get_type(self):
        return self.__types
