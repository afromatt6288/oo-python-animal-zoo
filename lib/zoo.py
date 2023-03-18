# from lib.zoo import Zoo

from lib.animal import Animal


class Zoo:

    animals_from_Animal = Animal.all
    all = []

    def __init__(self, name, location):
        if self.check_zoo(name):
            print("Zoo already exists.")
        elif type(name) is not str:
            print("Zoo name must be a string.")  
        elif type(location) is not str:
            print("Zoo location must be a string.")
        else:
            self.name = name
            self.location = location
            self.animals = []
            self.animal_species = []
            self.animal_nicknames = []
            self.add_to_zoo_animals(self)
            self.add_to_zoo_species(self)
            self.add_to_zoo_nicknames(self)
            Zoo.add_to_zoo_list(self)
    
    def get_zoo_name(self):
        return self._name
    
    def set_zoo_name(self, name):
        if type(name) is not str:
            print("Zoo name must be a string.")    
        else:
            print(f"Setting name to {name}.")
            self._name = name

    name = property(get_zoo_name, set_zoo_name)

    def get_zoo_location(self):
        return self._location
    
    def set_zoo_location(self, location):
        if type(location) is not str:
            print("Zoo location must be a string.")
        else:
            print(f"Setting location to {location}.")
            self._location = location
    
    location = property(get_zoo_location, set_zoo_location)

    @classmethod
    def check_zoo(cls, name):
        for zoo in cls.all:
            if name == zoo.name:
                return True            
    
    @classmethod
    def add_to_zoo_list(cls, self):
        cls.all.append(self)
    
    @classmethod
    def show_all_zoos(cls):
        for zoo in cls.all:
            print("Showing Zoo")
            print(f"{zoo.name}: {zoo.location}")
    
    @classmethod
    def find_by_location(cls, location):
        location_list = []
        for zoo in cls.all:
            if location == zoo.location:
                location_list.append(zoo.name)
        return location_list
    
    @classmethod
    def update_animals_list(cls):
        cls.animals_from_Animal = Animal.all

    @classmethod
    def add_to_zoo_animals(cls, self):
        for animal in cls.animals_from_Animal:
            if animal.zoo == self.name:
                self.animals.append(animal)
    
    @classmethod
    def add_to_zoo_species(cls, self):
        for animal in self.animals:
            if animal.species not in self.animal_species:
                self.animal_species.append(animal.species)

    @classmethod
    def add_to_zoo_nicknames(cls, self):
        for animal in self.animals:
            if animal.nickname not in self.animal_nicknames:
                self.animal_nicknames.append(animal.nickname)

    @classmethod
    def print_all_animals(cls):
        print(cls.animals_from_Animal)
        for animal in cls.animals_from_Animal:
            print("Showing Animal")
            print(f"Nickname:{animal.nickname}, Species:{animal.species}, Weight:{animal.weight} lbs, Zoo Location:{animal.zoo}")
    
    def print_animals_in_zoo(self):
        for animal in self.animals:
            print(f"Nickname:{animal.nickname}, Species:{animal.species}, Weight:{animal.weight} lbs")

    def find_by_species(self, species):
        species_list = []
        for animal in self.animals:
            if species == animal.species:
                species_list.append(animal)
        for animal in species_list:
            print(f"{animal.nickname}: {animal.species}")
        return species_list




# Sample Zoos
# san_fransisco_zoo = Zoo("San Fransisco Zoo", "San Fransisco, CA")
# san_diego_zoo = Zoo("San Diego Zoo", "San Diego, CA")
# denver_zoo = Zoo("Denver Zoo", "Denver, CO")
# other_denver_zoo = Zoo("Other Denver Zoo", "Denver, CO")
# bob_villa_zoo = Zoo("Bob Villa Zoo", "Boise, ID")