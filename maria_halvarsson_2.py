# Name: Maria Halvarsson
# Date: 2021-02-13
# Course code: DD100N
# This program allows the user to convert a value from one unit to another.
# There are three different convertions to choose from:
# 1. Meters to American miles, 2. Liters to gallons and 3. Pounds to kilograms.

# Converts meters to American miles
def meters_to_miles(meter):
    return meter / 1609.3

# Converts liters to gallons
def liters_to_gallons(liter):
    return liter / 3.785

# Converts pounds to kilograms
def pounds_to_kilos(pound):
    return pound * 2.2046

print("Hello!")
user_choice = "0"

while user_choice == "0":
    print("Choose which convertion you want to do by entering a number between 1-3.")
    print("To quit the program enter number 4.")
    print("1. Meters to American miles")
    print("2. Liters to gallons")
    print("3. Pounds to kilograms")
    print("4. Quit")
    user_choice = (input("Enter your choice: "))

    if user_choice == "1":
        user_input = float(input("Enter the number of meters: "))
        print(str(user_input) + " meters equals " + 
            str(round(meters_to_miles(user_input), 2)) + " American miles.\n")
        user_choice = "0"

    elif user_choice == "2":
        user_input = float(input("Enter the number of liters: "))
        print(str(user_input) + " liters equals " + 
            str(round(liters_to_gallons(user_input), 2)) + " gallons.\n")
        user_choice = "0"

    elif user_choice == "3":
        user_input = float(input("Enter the number of pounds: "))
        print(str(user_input) + " pounds equals " + 
            str(round(pounds_to_kilos(user_input), 2)) + " kilograms.\n")
        user_choice = "0"

    elif user_choice == "4":
        print("Program closed.\n")
        break

    else:
        print("Please enter a valid number\n")
        user_choice = "0"
