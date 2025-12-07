from random import randint
from random import choice
from weapon import Weapon
from potion import Potion


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
        self.__weapon: "Weapon" | None = None
        self.__buffs: list[tuple[str, int, int]] = []
        self.__potions: list[Potion] = []

    def modifier(self) -> int:
        if self.weapon.w_type == "melee":
            value = self.effective_strength
        else:
            value = self.effective_dexterity
        return (value - 10) // 2

    def is_alive(self) -> bool:
        if self.health <= 0:
            return False
        else:
            return True

    def __take(self, damage: int) -> int:
        self.health = self.__clamp_health(self.health - damage)
        return damage
    
    def __calculate_damage(self) -> int:
        return self.weapon.get_damage() + self.modifier()

    def attack(self, enemy: "Player")-> int:
        if self.weapon == None:
            damage = 1 + self.modifier()
        else:
            damage = self.calculate_damage
        if damage < 0:
            damage = 0
        damage = enemy.take(damage)
        return damage

    def heal(self, amount: int) -> int:
        self.health = self.__clamp_health(self.health + amount)
        return amount

    def add_buff(self, stat: str, amount: int = randint(1, 4), duration: int = randint(1, 3)) -> None:
        if stat == "strength":
            self.strength += amount
        elif stat == "dexterity":
            self.dexterity += amount
        self.__buffs.append((stat, amount, duration))

    def tick_buffs(self) -> None:
        self.__buffs = [(stat, amount, duration - 1) for stat, amount, duration in self.__buffs if duration > 1]

    def __str__(self):
        return (f"[{self.name}] \nForza: {self.strength}\nDestrezza: {self.dexterity}\n"
                f"HP massimi: {self.max_health}\nHP attuali: {self.health}")
    
    def use_potion(self, potion: Potion) -> dict:
        if potion not in self.__potions:
            return {"error": "potion_not_in_inventory"}
        
        result = potion.apply_to(self)
        
        if result and "error" not in result:
            self.__potions.remove(potion)
        
        return result
    
    def should_use_potion(self) -> Potion | None:
        if self.health <= 30:
            for potion in self.__potions:
                if potion.effect == "heal":
                    self.use_potion(potion)
                    return potion
                
        for potion in self.__potions[:]:
            if potion.effect in ("buff_str", "buff_dex"):
                self.use_potion(potion)
                return potion
        
        return None

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, new_name: str) -> None:
        if new_name == "":
            print("Non puoi rinominare il giocatore con il nulla")
            return
        self.__name = new_name

    @property
    def max_health(self) -> int:
        return self.__max_health

    @property
    def health(self) -> int:
        return self.__health

    def __clamp_health(self, value: int) -> int:
        return max(0, min(value, self.__max_health))

    @health.setter
    def health(self, new_health: int) -> None:
        self.__health = self.__clamp_health(new_health)


    @property
    def strength(self) -> int:
        return self.__strength

    @strength.setter
    def strength(self, new_strength: int) -> None:
        if new_strength > 20:
            self.__strength = 20
            print("Hai inserito un valore di forza più alto di 20! La forza è stata impostata al suo massimo.")
            return

        if new_strength < 1:
            self.__strength = 1
            print("Hai inserito un valore di forza più basso di 1! La forza è stata impostata al suo minimo.")
            return

        self.__strength = new_strength

    @property
    def dexterity(self) -> int:
        return self.__dexterity

    @dexterity.setter
    def dexterity(self, new_dexterity: int) -> None:
        if new_dexterity > 20:
            self.__dexterity = 20
            print("Hai inserito un valore di destrezza più alto di 20! La destrezza è stata impostata al suo massimo.")
            return

        if new_dexterity < 1:
            self.__dexterity = 1
            print("Hai inserito un valore di destrezza più basso di 1! La destrezza è stata impostata al suo minimo.")
            return
        self.__dexterity = new_dexterity

    @property
    def weapon(self) -> Weapon | None:
        return self.__weapon
    
    @weapon.setter
    def weapon(self, weapon: Weapon) -> None:
        self.__weapon = weapon

    @property
    def potions(self) -> list[Potion]:
        return self.__potions

    @potions.setter
    def potions(self, new_potions: list) -> None:
        if not isinstance(new_potions, list):
            print("Le pozioni devono essere una lista!")
            return
        
        for potion in new_potions:
            if not isinstance(potion, Potion):
                print(f"Errore: {potion} non è una Potion valida!")
                return
        
        if len(new_potions) > 3:
            print("Puoi avere massimo 3 pozioni nell'inventario!")
            return
        
        self.__potions = new_potions

    @property
    def buffs(self) -> list[tuple[str, int, int]]:
        return self.__buffs

    @property
    def effective_strength(self) -> int:
        base_strength = self.strength
        for stat, amount, duration in self.__buffs:
            if stat == "strength" and duration > 0:
                base_strength += amount
        return base_strength

    @property
    def effective_dexterity(self) -> int:
        base_dexterity = self.dexterity
        for stat, amount, duration in self.__buffs:
            if stat == "dexterity" and duration > 0:
                base_dexterity += amount
        return base_dexterity
    
    @property
    def take(self) -> int:
        return self.__take
    
    @property
    def calculate_damage(self) -> int:
        return self.__calculate_damage()