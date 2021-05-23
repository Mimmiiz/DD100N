# Titel: Platsbokning på SJ
# Uppgifts nr: 127
# Författare: Maria Halvarsson
# Datum: 2021-05-10
#
# This program helps with ticket booking on SJ trains.
# The screen will display an image of how the train looks like
# and the seats available for booking.
# Booked seats are marked with two '*' surroudning the seat number.
# The program offers functions such as booking, cancel booking, and
# display the most recently booked tickets.
# When a ticket is booked, it is saved to a ticket text file.
# All functions are not implemented yet.

# A class that defines a ticket
#   seat_number - the booked seat number, integer
#   train_number - the train number, integer
#   train_ride_number - the number of the train ride, integer

import math
import re

class Ticket:

    def __init__(self, seat, train, train_ride, train_cart):
        """Creates a new ticket.
        Parameters: self, seat (Seat object), train (Train object), train_ride (TrainRide object), 
        train_cart (TrainCart object)
        Return: nothing"""
        self.seat = seat
        self.train = train
        self.train_ride = train_ride
        self.train_cart = train_cart

    def __repr__(self):
        """Returns a string representation of a ticket.
        Parameters: self
        Return: A string representation of a ticket."""
        repr = ("PLATSBILJETT\n" + str(self.train_ride) + "\tPlats: " + str(self.seat.seat_number)) 
        return repr

# A class that defines a train ride, contains all the train ride information
# such as departure and arrival time and departure location and destination.
#   train_ride_number - the number of the train ride, integer
#   departure_location - the departure location of the train ride, string
#   destination - the destination of the trane ride (arrival location), string
#   departure_time - the departure time, string 
#   arrival_time - the arrival time, string
#   train_number - the train number of the train, integer
#   price - the price of the train ride, float

class TrainRide:

    def __init__(self, train_ride_number, departure_location, destination, departure_time, arrival_time, train_number, price):
        """Creates a new train ride.
        Parameters: self, train_ride_number (int), departure_location (string), destination (string), departure_time (string), 
        arrival_time (string), train_number (int), price (float)
        Return: nothing"""
        self.train_ride_number = train_ride_number
        self.departure_location = departure_location
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.train_number = train_number
        self.price = price

    def __repr__(self):
        """Returns a string representation of a train ride.
        Parameters: self
        Return: A string represenation of a train ride"""
        repr = (self.departure_location + " -> " + self.destination
        + "\nAvg. tid: " + self.departure_time + "\nAnk. tid: " + self.arrival_time
        + "\nTåg: " + str(self.train_number))
        return repr      

# A class that contains a list of train rides to be able to store
# multiple train rides.
#   train_rides - a list of TrainRide objects
class TrainRideList:

    def __init__(self, train_rides):
        """Creates a new train ride list
        Parameters: self, train_rides (a list of TrainRide objects)
        Return: nothing"""
        self.train_rides = train_rides

    def find_train_ride_number(self, train_ride_number):
        """Searches for a train ride number.
        Parameters: self, train_ride_number (int)
        Return: found_train_ride (a train ride that matches the searched train ride number)"""
        pass

    def find_train_number(self, train_number):
        """Searches för a train number.
        Parameters: self, train_number (int)
        Return: found_train_ride (a train ride that matches the searched train ride number)"""
        pass

    def add_train_ride(self, train_ride):
        """Adds a new train ride to the list.
        Parameters: self, train_ride (TrainRide object)
        Return: nothing"""
        pass

    def delete_train_ride(self, train_ride):
        """Deletes a train ride from the list.
        Parameters: self, train_ride (TrainRide object)
        Return: nothing"""
        pass 

# A class that defines a train
# train_number - int
# name - string
# train_carts - a list of TrainCart objects

class Train:

    def __init__(self, train_number, name, train_carts):
        """Creates a new train.
        Parameters: self, train_number (int), name (string), train_carts (a list of TrainCart objects)
        Returns: nothing"""
        self.train_number = train_number
        self.name = name
        self.train_carts = train_carts

    def __repr__(self):
        """Returns a string representation of a Train
        Parameters: self
        Returns: A string that represents the Train
        """
        return "Tågnummer: " + str(self.train_number) + "\nTågnamn: " + self.name


# A class that defines a train cart
#   train_cart_number - int
#   seats - a list containing Seat objects

class TrainCart:

    def __init__(self, train_cart_number, seats):
        """Creates a new train cart.
        Parameters: self, seats (a list of Seat objects)
        Return: nothing"""
        self.train_cart_number = train_cart_number
        self.seats = seats

    def __repr__(self):
        """Returns a string that represents the train cart.
        Parameters: self
        Returns: A string that represents the train cart"""
        rows = math.ceil(len(self.seats) / 4)
        repr = "┏"
        line = ""
        for i in range(0, rows):
            line = line + "━━━━"
        repr = repr + line + "┓\n┃"
        for i in range(0, 4):
            for seat in self.seats:
                if seat.seat_number % 4 == (i + 1) % 4:
                    if seat.seat_number <= 9:
                        repr = repr + (" ")
                    repr = repr + str(seat)
            if i == 1:
                repr = repr + "┃\n┣" + line + "┫\n┣" + line + "┫\n┃"
            elif i == 3:
                repr = repr + "┃\n┗" + line + "┛"
            else:
                repr = repr + "┃\n┃"
        return repr

    def number_of_available_seats(self):
        """Returns the number of available seats.
        Parameters: self
        Returns: available_seats (int)."""
        available_seats = 0
        for seat in self.seats:
            if seat.is_available():
                available_seats += 1
        return available_seats

    def book_seat(self, seat_number):
        """Book a selected seat. Returns the booked Seat if booking is successful.
        Parameters: self, seat_number (int)
        Returns: booked_seat (a Seat)"""
        seat = self.get_seat(seat_number)
        booked_seat = None
        if seat.is_available():
            seat.book()
            booked_seat = seat
        else:
            print("Platsen är redan bokad.")
        return booked_seat

    def cancel_booked_seat(self, seat_number):
        """Cancels a booked seat.
        Parameters: self, seat_number (int)
        Returns: nothing"""
        seat = self.get_seat(seat_number)
        if seat.is_available():
            print("Kan inte avboka en ledig plats. Försök igen.")
        else:
            seat.cancel()

    def get_seat(self, seat_number):
        """Returns a seat with the given seat number.
        Parameters: seat_number (int)
        Return: seat (a Seat)"""
        if seat_number > len(self.seats) or seat_number <= 0:
            raise IndexError("The index is out of bounds.")
        else:
            for seat in self.seats:
                if seat_number == seat.seat_number:
                    return seat

# A class that defines a seat
#   seat_number - the number of the seat, int
#   is_booked - is the seat booked or not? boolean

class Seat:
    
    def __init__(self, seat_number, is_booked = False):
        """Creates a new seat.
        Parameters: self, seat_number (int), is_booked (boolean)
        Returns: nothing"""
        self.seat_number = seat_number
        self.is_booked = is_booked

    def __repr__(self):
        """Returns a string that represents a seat.
        Parameters: self
        Returns: A string that represents a seat"""
        if self.is_booked:
            return "*" + str(self.seat_number) + "*"
        else:
            return " " + str(self.seat_number) + " "

    def book(self):
        """Books the seat.
        Parameters: self
        Returns: nothing"""
        self.is_booked = True

    def is_available(self):
        """Checks if a seat is available.
        Parameters: self
        Returns: True if the seat is available, else False"""
        return not(self.is_booked)

    def cancel(self):
        """Cancels the seat.
        Parameters: self
        Returns: nothing"""
        self.is_booked = False

#--------Functions--------

# Functions for saving train data might also be needed to not loose
# infromation when the program closes. 

def read_ticket_file(file_name):
    """Reads from a file with the given file name and creates a new list of ticket objects.
    Parameter: file_name (string)
    Return: tickets (a list of Ticket objects)"""
    pass

def read_train_file(file_name):
    """Reads from a file with the given file name and creates a new list of train objects.
    Parameter: file_name (string)
    Return: trains (a list of Train objects)"""
    file = open(file_name, "r")
    trains = []
    file_input = file.readline().strip()
    while file_input == 'Train':
        train_number = file.readline().strip()
        train_name = file.readline().strip()
        train_carts = []
        file_input = file.readline().strip()
        while file_input == 'Cart':
            train_cart_number = file.readline().strip()
            seats = read_seats_from_file(file) 
            train_carts.append(TrainCart(int(train_cart_number), seats))
            file_input = file.readline().strip()
        trains.append(Train(int(train_number), train_name, train_carts))
    return trains

def write_train_file(file_name, trains):
    """Writes the trains to a file with the fiven file name.
    Parameters: file_name (string), trains (a list of Train objects)
    Return: nothing"""
            
def read_seats_from_file(file):
    """Reads from a file and creates a new list of seat objects.
    Parameter: file (a file)
    Return: seats (a list of Seat objects)"""
    seats = []
    seat_number = file.readline().strip()
    while seat_number != "":
        is_booked = file.readline().strip()
        if is_booked == 'True':
            is_booked = True
        elif is_booked == 'False':
            is_booked = False
        seats.append(Seat(int(seat_number), is_booked))
        seat_number = file.readline().strip()
    return seats

def write_seats_to_file(file, seats):
    """Writes the seats to a file.
    Parameters: file (a file), seats (a list of Seat objects)
    Return: nothing"""
    for seat in seats:
        file.write(str(seat.seat_number) + "\n")
        file.write(str(seat.is_booked) + "\n")

def read_train_ride_file(file_name):
    """Reads from a file and creates a TrainRideList object from the given input.
    Parameter: file_name (string)
    Return: train_rides (a TrainRideList object)"""
    pass

def save_train_ride_file(file_name, train_rides):
    """Save the train rides to the train ride file. 
    Parameter: train_rides (a TrainRideList object)
    Return: nothing"""
    pass

def print_tickets(file_name, tickets):
    """Writes the booked tickets to a file with the given file name.
    Parameters: file_name (string), tickets (a list of Ticket objects)
    Return: nothing"""
    if len(tickets) == 0:
        print("Det finns inga bokade biljetter att skriva ut.")
    else:
        file = open(file_name, "w", encoding="utf-8")
        for ticket in tickets:
            file.write("********************\n")
            file.write(str(ticket) + "\n")
        file.close()

# Fixa: användaren ska inte kunna boka fler platser än som finns tillgängligt.
def book_tickets(number_of_tickets, train, train_ride):
    """Books the given number of tickets.
    Parameters: number_of_tickets (int)
    Return: tickets (a list of Ticket objects)"""
    tickets = []
    for i in range(0, number_of_tickets):
        print("Ange platsnumret du vill boka: ")
        seat_number = input()
        while(True):
            while(True):
                if is_integer(seat_number):
                    break
                else:
                    print("Vänligen ange ett korrekt platsnummer: ")
                    seat_number = input()
            try:
                seat = train.book_seat(int(seat_number))
                if seat == None:
                    print("Ange ett annat platsnummer: ")
                else:
                    tickets.append(Ticket(seat, train, train_ride))
                    break
            except IndexError:
                print("Vänligen ange ett korrekt platsnummer: ")
            seat_number = input()
        print(train)
    return tickets

def main_menu(train):
    """Displays the menu to the use.
    Parameters: train (a Train object)
    Return: nothing"""
    # hårdkodade värden för att kunna testa programmet
    train_ride = TrainRide(1, "Stockholm", "Göteborg", "14:00", "18:00", 1, 250.00)

    menu_choices = ("Vad vill du göra?\nBoka, skriv 'B', på samma rad följt av önskat antal biljetter (exempel B 2).\n" +
        "Avboka, skriv 'A', på samma rad följt av ett platsnummer (exempel A 10).\n" + 
        "Skriv ut de senaste bokade biljetterna, skriv 'S'.\nAvsluta, skriv Q.")
    tickets = []
    print(menu_choices)
    print(train)
    user_input = get_input(train)
    
    while user_input != 'Q':
        if user_input[0] == 'B':
            tickets = tickets + book_tickets(int(user_input[2:]), train, train_ride)
            print("")
        elif user_input[0] == 'A':
            try:
                train.cancel_booked_seat(int(user_input[2:]))
            except IndexError:
                print("Det angivna platsnumret är ogiltigt, försök igen.")
            print("")
        elif user_input == 'S':  
            print_tickets("tickets.txt", tickets)
        print(menu_choices)
        print(train)
        user_input = get_input(train)

def get_input(train):
    """Gets the input from the user and returns the choice.
    Parameters: train (a Train object)
    Return: user_input (string)"""
    while True:
        try:
            user_input = input("Ange ett val: ")
            if user_input == 'S' or user_input == 'Q':
                break
            elif re.match("^B\s[0-9]+$|^A\s[0-9]+$", user_input):
                if int(user_input[2:]) <= 0 or int(user_input[2:]) > len(train.seats):
                    print("Du måste ange ett nummer mellan 1 och " + str(len(train.seats)) + ". Vänligen ange nytt val.")
                if user_input[0] == 'B' and int(user_input[2:]) > train.number_of_available_seats():
                    print("Du kan inte boka fler platser än de som finns tillgängliga. Vänligen ange nytt val.")
                else:
                    break
            else:
                print("Vänligen ange ett giltigt val.")
        except IndexError or AttributeError:
                print("Vänligen ange ett giltigt val.")
    
    return user_input

def is_integer(val):
    """Checks if a value is an integer.
    Parameters: val (unknown type)
    Return: True if the value is an integer, else False"""
    try:
       int(val)
       return True
    except ValueError:
        return False    

# Main function
def main():
    #seats = read_seats_file("seats.txt")
    trains = read_train_file("train.txt")
    print(str(trains[0]))
    print(str(trains[0].train_carts[0]))
    print(str(trains[0].train_carts[1]))
    print(str(trains[0].train_carts[2]))
    print(str(trains[0].train_carts[3]))
    print(str(trains[1].train_carts[0]))
    print(str(trains[1].train_carts[2]))
    print("Välkommen till SJ:s platsbokning.")
    #main_menu(train)
    #write_seats_file("seats.txt", seats)

    """The main function
    Algorithm:
    1. Welcome the user.
    2. Read data from the files.
    3. Display all options in a menu.
    4. The user can choose an option or quit the program.
    5. If the user does not choose to quit, they can continue to choose an option
    6. Step 3-5 is repeated until the user quits.
    7. Save data and quit program
    """

main()