#Import main program
from Pet import*
#Create a class for Run
class Run:
#Create main function
    def main():
#Create a variable for the pet class
        petinfo = Pet()

#Ask the user to input pet details
        name = input("Enter the name of your pet: ")
        animal_type = input("Enter the type of your pet (e.g., Dog, Cat, Bird): ")
        age = int(input("Enter the age of your pet: "))

#Set input details to class
        petinfo.set_name(name)
        petinfo.set_animal_type(animal_type)
        petinfo.set_age(age)

#Print pet details
        print("Here are the details of your pet:")
        print("Pet Name:", petinfo.get_name())
        print("Animal Type:", petinfo.get_animal_type())
        print("Age:", petinfo.get_age())
        
#Start the function
