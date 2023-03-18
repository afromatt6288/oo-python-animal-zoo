# from lib.animal import Animal

class Animal:

    all = []
    animal_species = []

    def __init__(self, nickname, species = "Unknown", weight = 0, zoo = "TBD"):
        if self.check_animal_nickname(nickname):
            print("Animal already exists.")
        elif type(nickname) is not str:
            print("Animal Nickname must be a string")
        elif type(species) is not str:
            print("Animal Species must be a string")
        elif type(weight) is not int:
            print("Animal Weight must be an Integer.")  
        elif type(zoo) is not str:
            print("Animal Zoo must be a string")
        else:
            print(f"Welcome {nickname} to {zoo}! You are a(n) {species}, and weigh {weight} lbs. We are glad to have you!")
            self._nickname = nickname                
            self.species = species
            self.weight = weight
            self.zoo = zoo
            Animal.add_to_animal_list(self)
            Animal.update_species_list(species)  
    
    def get_animal_nickname(self):
        return self._nickname
    
    def set_animal_nickname(self, nickname):
        if self.check_animal_nickname(self.nickname):
            print("Cannot change Animal Nickname!")
        else:
            print(f"Setting Nickname to {nickname}")
            self._nickname = nickname
    
    nickname = property(get_animal_nickname, set_animal_nickname)

    def get_animal_species(self):
        return self._species
    
    def set_animal_species(self, species):
        if self.check_animal_nickname(self.nickname):
            print("Cannot change Animal Species!")
        else:
            print(f"Setting Species to {species}")
            self._species = species
    
    species = property(get_animal_species, set_animal_species)

    def get_animal_weight(self):
        return self._weight
    
    def set_animal_weight(self, weight):
        if type(weight) is not int:
            print("Animal Weight must be an Integer.")   
        else:
            print(f"Setting Weight to {weight}")
            self._weight = weight
    
    weight = property(get_animal_weight, set_animal_weight)

    def get_animal_zoo(self):
        return self._zoo
    
    def set_animal_zoo(self, zoo):
        if type(zoo) is not str:
            print("Animal Zoo must be a string")
        else:
            print(f"Setting Zoo to {zoo}")
            self._zoo = zoo
    
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
        if species in cls.animal_species:
            print(f"{species} already listed.")
        else:
            print(f"New Species ({species}) Found!")
            cls.animal_species.append(species) 
    
    # @classmethod
    # def animal_species(cls):
    #     return animal_species

    
    @classmethod
    def find_by_species(cls, species):
        animal_species = []
        for animal in cls.all:
            if species == animal.species:
                animal_species.append(animal)
        for animal in animal_species:
            print(f"Nickname:{animal.nickname}, Species:{animal.species}, Weight:{animal.weight} lbs, Zoo Location:{animal.zoo}")
        return animal_species
    
    @classmethod
    def show_all_animals(cls):
        print("Showing All Animals")
        for animal in cls.all:
            print(f"Nickname:{animal.nickname}, Species:{animal.species}, Weight:{animal.weight} lbs, Zoo Location:{animal.zoo}")
        return cls.all



# Sample Animals
gertie = Animal("Gertie", "Giraffe", 200, "San Diego Zoo")
ellie = Animal("Ellie", "Elephant", 500, "Denver Zoo")
william = Animal("William", "Wolf", 80, "San Fransisco Zoo")
george = Animal("George", "Gorilla", 320, "San Diego Zoo")
elijah = Animal("Elijah", "Elephant", 530, "Denver Zoo")
artie = Animal("Artie", "Aardvark", 20, "San Fransisco Zoo")
peppe = Animal("Peppe", "Penguin", 9, "Other Denver Zoo")
larry = Animal("Larry", "Lemur", 6, "Bob Villa Zoo")
