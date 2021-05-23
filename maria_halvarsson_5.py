# Name: Maria Halvarsson
# Date: 2021-03-29
# Course code: DD100N7

# This program stores the name and points of darts players. Each player gets to throw five darts and can 
# get a maximum total of 50 points. A player can not get deduction of their score if they miss.
# The player's results are written to a file whe the program is closed.
# New players and their scores can be added, but they can not have the same name as an existing player.
# The scores of all players can be viewed and will be ordered from highest to lowest score.

# the name of the file to read and write to
FILE_NAME = "results.txt"

def read_file(file_name):
    """ Reads from a file with the given file name and stores the values in a matrix as
    a row with values [person, score].
    Paramter: file_name (string)
    Return: results (matrix where each row contains values [person, score])"""
    file = open(file_name, "r")
    results =   []
    person = file.readline().strip()
    while person != "":
        score = int(file.readline().strip())
        results.append([person, score])
        person = file.readline().strip()
    file.close()
    return results

def view_results(results):
    """Prints out the results in size order to the user.
    Parameter: results (matrix where each row contains values [person, score])
    Return: nothing"""

    results = sorted(results, key = lambda score: score[1], reverse = True)
    for result in results:
        print(result[0] + " " + str(result[1]) + " points")
        
def add_result(results):
    """ Adds a new player and their score to the results. The user can not enter a player name
    that already exists. The user will get a new chance to enter a new name if they enter an
    existing name. The score entered has to be an integer, if the user enters an illegal value
    they will get a new chance to enter a value.
    Parameters: results (matrix where each row contains values [person, score])
    Return: results (matrix where each row contains values [person, score])"""
    person = input_name(results)
    score = input_score()
    results.append([person, score])
    return results

def input_name(results):
    """ Returns the name of the player that is entered by the user. The user can not enter a name
    that already exists and will get a new chance if they do.
    Parameters: results (matrix where each row contains values [person, score])
    Return: name (string)"""
    name = input("Enter the name of the player: ")
    while not name.strip():
        name = input("That is not a valid name, please enter a new one: ")
    if len(results) == 0:
        return name
    else:
        valid = False
        while not valid:
            counter = 0
            for result in results:
                counter += 1
                if result[0] == name:
                    name = input("The name " + name + " already exists. Please enter another name: ")
                    while not name.strip():
                        name = input("That is not a valid name, please enter a new one: ")
                    break
                elif counter == len(results):
                    valid = True
    return name
                  
def input_score():
    """Retruns the score of the player that the user enters. If the user enters an invalid score, they
    will get a new chance of entering a valid score. The score must be an integer between 0-50.
    Parameters: none
    Return: score (integer)"""
    while True:
        score = input("Enter the score: ")
        if is_integer(score) == True:
            if int(score) < 0 or int(score) > 50:
                print("The entered score is not valid, the score must be between 0-50. Please try again.")
            else:
                break
        else:
            print("The entered value is not a number, please try again.")
    return int(score)

def save_results(file_name, results):
    """Saves the result from the matrix to the file with the given file name.
    Parameters: file_name (string), results (matrix where each row contains values [person, score])
    Return: nothing"""
    file = open(file_name, "w")
    for result in results:
        file.write(result[0] + "\n")
        file.write(str(result[1]) + "\n")
    file.close()

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

def is_integer(val):
    """Checks if a value is an integer.
    Parameters: val (unknown type)
    Return: True if the value is an integer, else False"""
    try:
       int(val)
       return True
    except ValueError:
        return False 

def main():
    """ This function is the main function where the program starts.
    The main function lets the user choose different options between 1-3.
    Parameters: none
    Return: nothing
    """
    print("Welcome to the yearly darts competition!")
    print("Main menu\n1. View results\n2. Add new result\n3. Save and quit")
    user_input = get_input()
    results = read_file(FILE_NAME) 
    while user_input != 3:

        if user_input == 1:
            print("")
            view_results(results)
            print("")

        elif user_input == 2:
            print("")
            add_result(results)
            print("")
            
        print("Main menu\n1. View results\n2. Add new result\n3. Save and quit")
        user_input = get_input()

    save_results(FILE_NAME, results)
    print("\nThe results have been saved.")
    
main()
