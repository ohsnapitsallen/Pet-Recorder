#Create class pet
class Pet:
#Create a constructor
    def __init__(self, name = ' ', animal_type = ' ', age = 0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
#Create setters
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age
#Create getters
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age
