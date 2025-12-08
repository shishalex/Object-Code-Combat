class Potion:
    __allowed_effects = {"heal", "buff_str", "buff_dex"}

    def __init__(self, name: str, effect: str, amount: int, duration: int):
        if name == "":
            raise ValueError("Il nome non può essere una stringa vuota!")
        if effect not in Potion.__allowed_effects:
            raise ValueError("La Pozione non ha un effetto valido!")
        if amount < 1:
            raise ValueError("La Pozione non può avere un valore minore o pari a 0!")

        self.__name = name
        self.__effect = effect
        self.__amount = amount
        self.__duration = duration
        self.__used = False

    def apply_to(self, target)-> dict:
        if self.used:
            raise ValueError("Questa pozione non è utilizzabile!")
        
        elif self.effect == "heal":
            if hasattr(target, "heal") and callable(getattr(target, "heal")):
                if target.health == target.max_health:
                    raise ValueError(f"{target.name} ha già gli HP al massimo!")
                target.heal(self.amount)
                self.used = True
            else:
                raise ValueError("Il Target non può usare la pozione!")

        elif self.effect in ("buff_dex", "buff_str"):
            if hasattr(target, "add_buff") and callable(getattr(target, "add_buff")):
                effect_type = "strength" if self.effect == "buff_str" else "dexterity"
                if any(buff[0] == effect_type for buff in target.buffs):
                    raise ValueError(f"{target.name} ha già un buff di {effect_type} attivo!")
                
                target.add_buff(effect_type, self.amount, self.duration)
                self.used = True
            else:
                raise ValueError("Il Target non può usare la pozione!")
            
        return {"effect":self.effect, "amount":self.amount, "duration":self.duration}

    def __str__(self):
        if self.effect == "heal":
            return f"{self.name}({self.effect} +{self.amount})"
        else:
            return f"{self.name}({self.effect} +{self.amount} for {self.duration} turns)"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if new_name == "":
            print("Non puoi rinominare la pozione con il nulla")
            return
        self.__name = new_name

    @property
    def effect(self):
        return self.__effect

    @effect.setter
    def effect(self, new_effect: str):
        if new_effect not in Potion.__allowed_effects:
            print(
                f"Valore non valido per 'effect': '{new_effect}'. "
                f"I valori ammessi sono: {', '.join(Potion.__allowed_effects)}"
            )
            return
        self.__effect = new_effect

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, new_amount: int):
        if new_amount < 1:
            print("Il numero di pozioni non può essere minore di 1!"
                  "Il numero ora è 1!")
            self.__amount = 1
            return

        self.__amount = new_amount

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, new_duration: int):
        if self.effect == "heal":
            self.__duration = 0
            return
        self.__duration = new_duration
    
    @property
    def used(self):
        return self.__used

    @used.setter
    def used(self, new_used: bool):
        self.__used = new_used
