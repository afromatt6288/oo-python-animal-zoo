# from lib.zoo import Zoo
# Sample Zoos
# SanFranZoo = Zoo("San Fransisco Zoo", "San Fransisco, CA")
# SanDiegoZoo = Zoo("San Diego Zoo", "San Diego, CA")
# DenZoo = Zoo("Denver Zoo", "Denver, CO")
# OtherDenZoo = Zoo("Other Denver Zoo", "Denver,CO")

from lib.animal import Animal

class Zoo:

    all = []
    animals = []

    def __init__(self, name, location):
        if self.check_zoo(name):
            print("Zoo already exists.")
        else:
            self.name = name
            self.location = location
            Zoo.add_to_zoo_list(self)
    
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