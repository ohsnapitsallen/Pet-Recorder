#Import main program
from Pet import*
#Create a class for Run
class Run:
#Create main function
    def main():
#Create a variable for the pet class
        petinfo = Pet()

#Ask the user to input pet details
        name = input("What is the name of your pet?: ")
        animal_type = input("What kind of animal is your pet?: ")
        age = int(input("How old is your pet: "))
#Set input details to class
#Print pet details
#Start the function
