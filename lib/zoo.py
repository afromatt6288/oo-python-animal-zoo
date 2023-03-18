# from lib.zoo import Zoo

from lib.animal import Animal

animals_from_Animal = [Animal.all]
animal_species_from_Animal = [Animal.species_list]

class Zoo:

    all = []

    def __init__(self, name, location):
        if self.check_zoo(name):
            print("Zoo already exists.")
        else:
            self.name = name
            self.location = location
            Zoo.add_to_zoo_list(self)
            Zoo.add_to_zoo_animals(self)
    
    def get_zoo_name(self):
        return self._name
    
    def set_zoo_name(self, name):
        if type(name) is str:
            print(f"Setting name to {name}.")
            self._name = name
        else:
            print("Zoo name must be a string.")    

    name = property(get_zoo_name, set_zoo_name)

    def get_zoo_location(self):
        return self._location
    
    def set_zoo_location(self, location):
        if type(location) is str:
            print(f"Setting location to {location}.")
            self._location = location
        else:
            print("Zoo location must be a string.")
    
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
    
    # @classmethod
    # def update_animals_list(cls):
    #     cls.animals_from_Animal.append(Animal.all)
    #     cls.animal_species_from_Animal.append(Animal.species_list)

    @classmethod
    def add_to_zoo_animals(self, animals):
        animals = []
        for animal in animals_from_Animal:
            if animal.zoo == self.name:
                animals.append(animal.zoo)

    @classmethod
    def print_all_animals(cls):
        print(cls.animals)




# Sample Zoos
# san_fransisco_zoo = Zoo("San Fransisco Zoo", "San Fransisco, CA")
# san_diego_zoo = Zoo("San Diego Zoo", "San Diego, CA")
# denver_zoo = Zoo("Denver Zoo", "Denver, CO")
# other_denver_zoo = Zoo("Other Denver Zoo", "Denver, CO")
# bob_villa_zoo = Zoo("Bob Villa Zoo,", "Boise, ID")