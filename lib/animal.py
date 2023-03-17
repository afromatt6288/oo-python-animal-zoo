# from lib.animal import Animal
# Sample Animals
# Gertie = Animal("Gertie", "Giraffe", 200, "SanDeigoZoo")
# Ellie = Animal("Ellie", "Elephant", 500, "DenZoo")
# William = Animal("William", "Wolf", 80, "SanFranZoo")
# George = Animal("George", "Gorilla", 320, "SanDiegoZoo")
# Elijah = Animal("Elijah", "Elephant", 530, "DenZoo")
# Artie = Animal("Artie", "Aardvark", 20, "SanFranZoo")

class Animal:

    all = []
    species_list = []

    def __init__(self, nickname, species, weight, zoo):
        if self.check_animal_nickname(nickname):
            print("Animal already exists.")
        else:
            print(f"Welcome {nickname} to {zoo}! You are a(n) {species}, and weigh {weight} lbs. We are glad to have you!")
            self._nickname = nickname                
            self._species = species
            self.weight = weight
            self.zoo = zoo
            Animal.add_to_animal_list(self)
            Animal.update_species_list(species)  
    
    def get_animal_nickname(self):
        return self._nickname
    
    def set_animal_nickname(self, nickname):
        if self.check_animal_nickname(self.nickname):
            print("Cannot change Animal Nickname!")
        elif type(nickname) is str:
            print(f"Setting Nickname to {nickname}")
            self._nickname = nickname
        else:
            print("Animal Nickname must be a string")
    
    nickname = property(get_animal_nickname, set_animal_nickname)

    def get_animal_species(self):
        return self._species
    
    def set_animal_species(self, species):
        if self.check_animal_nickname(self.nickname):
            print("Cannot change Animal Species!")
        elif type(species) is str:
            print(f"Setting Species to {species}")
            self._species = species
        else:
            print("Animal Species must be a string")
    
    species = property(get_animal_species, set_animal_species)

    def get_animal_weight(self):
        return self._weight
    
    def set_animal_weight(self, weight):
        if type(weight) is int:
            print(f"Setting Weight to {weight}")
            self._weight = weight
        else:
            print("Animal Weight must be an Integer.")   
    
    weight = property(get_animal_weight, set_animal_weight)

    def get_animal_zoo(self):
        return self._zoo
    
    def set_animal_zoo(self, zoo):
        if type(zoo) is str:
            print(f"Setting Zoo to {zoo}")
            self._zoo = zoo
        else:
            print("Animal Zoo must be a string")
    
    zoo = property(get_animal_zoo, set_animal_zoo)
    
    @classmethod
    def check_animal_nickname(cls, nickname):
        for animal in cls.all:
            if nickname == animal.nickname:
                return True 

    @classmethod
    def add_to_animal_list(cls, self):
        cls.all.append(self)
    
    @classmethod
    def update_species_list(cls, species):
        if species in cls.species_list:
            print(f"{species} already listed.")
        else:
            print(f"New Species ({species}) Found!")
            cls.species_list.append(species) 
    
    @classmethod
    def show_all_animals(cls):
        for animal in cls.all:
            print("Showing Animal")
            print(f"Nickname:{animal.nickname}, Species:{animal.species}, Weight:{animal.weight} lbs, Zoo Location:{animal.zoo}")
