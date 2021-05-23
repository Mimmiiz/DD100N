# Name: Maria Halvarsson
# Date: 2021-04-11
# Course code: DD100N7

# This program represents a robot that takes care of your pets. The robot can feed and play with the pets.
# Each pet has a name, species, hunger and play need. The hunger and play need is an integer value
# that is between 0 and 10 where 10 is the hungriest or biggest need to play.
# The user can manipulate the wellbeing of the pets by choosing what the robot should do. 
# The data of the program is stored in a file that is read and written to.

# the name of the file to read and write to
FILE_NAME = "pets.txt"

class Pet:
    """Describes a pet with the attributes name (string), species (string), hunger (int) and play_need (int).
    The hunger is an integer between 0-10 and represents hunger level, the larger the value the hungrier.
    The play_need is an integer between 1-10 and represents play need where a larger value means that the need
    to play is bigger."""
    def __init__(self, name, species, hunger, play_need):
        """Constructor, called when creating a new pet instance.
        Parameters: name (str), species (str), hunger (int), play_need (int)"""

        if hunger < 0 or hunger > 10:
            raise ValueError("Could not create a new pet instance, hunger must be an integer between 0 and 10.")
        elif play_need < 0 or play_need > 10:
            raise ValueError("Could not create a new pet instance, play_need must be an integer between 0 and 10.")
            
        self.name = name #string
        self.species = species.lower() #string
        self.hunger = hunger #int
        self.play_need = play_need #int

    def __repr__(self):
        """Retruns a string representation of the object."""
        return "The " + self.species + " " + self.name + ", Hunger: " + str(self.hunger)+ ", Play need: " + str(self.play_need)

    def __lt__(self, other):
        """Compares two pets based firstly on species and secondly on name. 
        This method is used when sorting"""
        if self.species < other.species:
            return True
        elif self.species == other.species:
            if self.name < other.name:
                return True
            else: return False
        else:
            return False

    def feed(self, hunger_points):
        """Feeds the pet according to given number of hunger points, if the hunger points exceed 
        the pets hunger the pet will only be fed as much as it needs.
        The hunger of the pet will be updated depending on the hunger points it was fed.
        Parameters: self, hunger_points (int)
        Return: nothing """
        if hunger_points < 1 or hunger_points > 10:
            raise ValueError("The integer value has to be between 1 and 10.")
        else:
            if self.hunger < hunger_points:
                self.hunger = 0
            else:
                self.hunger = self.hunger - hunger_points
    
    def play(self, play_time):
        """Plays with the pet for the given play time (in minutes).
        10 min of play time will decrease the play need of the pet by 1.
        If a pet plays for less than 10 min it will not affect the play need.
        Parameters: self, play_time (int)
        Return: nothing """
        if play_time < 1:
            raise ValueError("The integer value has to be positive.")
        else:
            play_time = play_time // 10
            if self.play_need < play_time:
                self.play_need = 0
            else:
                self.play_need = self.play_need - play_time

def display_pets(pets):
    """Displays all pets in the list by sorting the pets firstly by species
    and secondly by name.
    Parameters: pets (a list of Pets)
    Return: nothing"""
    print("All pets sorted by species and name: ")
    pets.sort()
    for pet in pets:
        print(pet)

def find_pet(pets, name):
    """Find the pet with the given name from a list of Pets.
    Parameters: pets (a list of Pets), name (string)
    Return: pet (Pet)"""
    for pet in pets:
        if pet.name == name:
            return pet

def feed_pet(pet):
    """Feeds the specified pet by asking the user to enter a number of hunger points.
    The hunger points entered must be an integer value between 1-10.
    If the user enters an invalid value they will be notified until a valid value is entered.
    Parameters: pet (Pet)
    Return: nothing """
    pet.name
    print("\nEnter the number of hunger points to feed " + pet.name + ": ")
    hunger_points = input()
    while True:
        if is_integer(hunger_points) == True:
            try:
                pet.feed(int(hunger_points))
                print("Fed " + pet.name + ".\n")
                break
            except ValueError as e:
                print(e)
                print("Please try again: ")
                hunger_points = input()
        else:
            print("The value must be an integer. Please enter a new value: ")
            hunger_points = input()

def play_with_pet(pet):
    """Plays with the specified pet by asking the user to enter the play time.
    The user must enter a valid value or else they will be notified until a correct one is entered.
    Parameters: pet (Pet)
    Return: nothing """
    print("\n10 minutes if play will decrease the play need by 1.")
    print("Enter the number of minutes to play with " + pet.name + ": ")
    play_time = input()
    while True:
        if is_integer(play_time) == True:
            try:
                pet.play(int(play_time))
                print("Played with " + pet.name + ".\n")
                break
            except ValueError as e:
                print(e)
                print("Please try again: ")
                play_time = input()
        else:
            print("The value must be an integer. Please enter a new value: ")
            play_time = input()

def read_file(file_name):
    """Reads from a file with the given file name and creates new pet instances from the input.
    Parameter: file_name (string)
    Return: pets (a list of Pets)"""
    file = open(file_name, "r")
    pets = []
    name = file.readline().strip()
    while name != "":
        species = file.readline().strip()
        hunger = int(file.readline().strip())
        play_need = int(file.readline().strip())
        pets.append(Pet(name, species, hunger, play_need))
        name = file.readline().strip()
    file.close()
    return pets

def get_input():
    """This function lets the user enter an input option which is an integer that ranges from 1-3.
    If the user enters an invalid value they will be notified and they get a change of entering
    a new value. The value of the input is returned from the function.
    Parameters: none
    Return: user_input (integer)"""
    while True:
        user_input = input("Please choose an option: ")
        if is_integer(user_input) == True:
            if int(user_input) < 1 or int(user_input) > 3:
                print("Please enter a valid number.")
            else:
                break
        else: 
            print("The entered value is not a number, please try again.")
    return int(user_input)

def save_pets(file_name, pets):
    """ Saves the pets data from the list of pets to the file with the given file name.
    Input: file_name (string), pets (A list of Pets)
    Return: nothing """
    file = open(file_name, "w")
    for pet in pets:
        file.write(pet.name + "\n")
        file.write(pet.species + "\n")
        file.write(str(pet.hunger) + "\n")
        file.write(str(pet.play_need) + "\n")
    file.close()

def is_integer(val):
    """Checks if a value is an integer.
    Parameters: val (unknown type)
    Return: True if the value is an integer, else False"""
    try:
       int(val)
       return True
    except ValueError:
        return False

def main_menu(pets):
    """Displays the main menu to the user and allows the user to choose different options.
    Parameter: pets (A list of Pets)
    Return: nothing"""
    print("Main menu:\n1. List all pets and their status.\n2. Find pet\n3. Quit")
    user_input = get_input()
    while user_input != 3:

        if user_input == 1:
            print(" ")
            display_pets(pets)
            print(" ")
        
        elif user_input == 2:
            print("\nEnter pet name: ")
            name = str(input()).capitalize()
            pet = find_pet(pets, name)
            if pet == None:
                print("\nCould not find a pet with the name " + name + ".\n")
            else:
                print("Found " +  name + ".")
                pet_choice_menu(pet)
            
        print("Main menu:\n1. List all pets and their status.\n2. Find pet\n3. Quit")
        user_input = get_input()

def pet_choice_menu(pet):
    """Displays the pet choice menu to the user where the user can choose to feed or play with the pet.
    Parameters: pet (Pet)
    Return: nothing """
    print("What should I do now?\n1. Feed " + pet.name + "\n2. Play with " + pet.name + "\n3. Exit to main menu")
    user_input = get_input()
    while user_input != 3:

        if user_input == 1:
            feed_pet(pet)

        elif user_input == 2:
            play_with_pet(pet)

        print("What should I do now?\n1. Feed " + pet.name + "\n2. Play with " + pet.name + "\n3. Exit to main menu")
        user_input = get_input()

def main():
    """This is the main function of the program where the program starts.
    Parameters: none
    Return: nothing """
    print("Hello, welcome to the PetRobo. What can I do for you?")
    pets = read_file(FILE_NAME)
    main_menu(pets)
    save_pets(FILE_NAME, pets)
    print("\nThe pet data has been saved. Program has closed.")

main()
    