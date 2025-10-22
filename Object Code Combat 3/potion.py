class Potion:
    __allowed_effects = {"heal", "buff_str", "buff_dex"}

    def __init__(self, name: str, effect: str, amount: int, duration: int):
        self.__name = name
        self.__effect = effect
        self.__amount = amount
        self.__duration = duration


    def apply_to(self):
        return


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
    def duration(self, new_duration):
        if self.effect == "heal":
            self.__duration = 0
            return

        self.__duration = new_duration
