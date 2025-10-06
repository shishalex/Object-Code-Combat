from random import randint

class Weapon:
    def __init__(self, name:str, min_damage:int, max_damage:int, types:str):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.types = types.lower

    
    def get_damage(self) -> int:
        return randint(self.min_damage, self.max_damage)
    
    def __str__(self):
        return f"{self.name} ({self.min_damage}-{self.max_damage} dmg)"