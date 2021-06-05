# Titel: Platsbokning på SJ
# Uppgifts nr: 127
# Författare: Maria Halvarsson
# Datum: 2021-06-06
#
# This program helps with ticket booking on SJ trains.
# The screen will display an image of how the train looks like
# and the seats available for booking.
# Booked seats are marked with two '*' surroudning the seat number.
# The program offers functions such as booking, cancel booking, and
# display the most recently booked tickets.
# All tickets booked during one program session can be saved to a ticket text file.
# After each session upon selecting quit (Q), the program data is saved to text files.

import math
import re
import datetime

# A class that defines a ticket
#   seat - the booked seat, Seat object
#   train_route - the booked train route, TrainRoute object
#   train_cart - the train cart that has the booked seat, TrainCart object
#   train - a Train object

class Ticket:

    def __init__(self, seat, train_route, train_cart, train):
        """Creates a new ticket.
        Parameters: self, seat (Seat object), train_route (TrainRoute object), train_cart (TrainCart object), train (Train object)
        Return: nothing"""
        self.seat = seat
        self.train_route = train_route
        self.train_cart = train_cart
        self.train = train

    def __repr__(self):
        """Returns a string representation of a ticket.
        Parameters: self
        Return: A string representation of a ticket."""
        repr = ("PLATSBILJETT\n" + str(self.train_route) + "\tTågnamn: " + str(self.train.name) + "\nPlats: " + str(self.seat.seat_number) 
            + "\tVagn: " + str(self.train_cart.train_cart_number)) 
        return repr

# A class that defines a train route, contains all the train route information
# such as departure and arrival time and departure location and destination.
#   train_route_number - the number of the train route, integer
#   departure_location - the departure location of the train route, string
#   destination - the destination of the train route (arrival location), string
#   departure_time - the departure time, datetime
#   arrival_time - the arrival time, datetime
#   train_number - the train number of the train, integer
#   price - the price of the train route, float
#   train_route_type - the train route type, for instance express or regional, string

class TrainRoute:

    def __init__(self, train_route_number, departure_location, destination, departure_time, arrival_time, train_number, price, train_route_type):
        """Creates a new train route.
        Parameters: self, train_route_number (int), departure_location (string), destination (string), departure_time (datetime), 
        arrival_time (datetime), train_number (int), price (float), train_route_type (string)
        Return: nothing"""
        self.train_route_number = train_route_number
        self.departure_location = departure_location
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.train_number = train_number
        self.price = price
        self.train_route_type = train_route_type

    def __repr__(self):
        """Returns a string representation of a train route.
        Parameters: self
        Return: A string represenation of a train route"""
        repr = (self.departure_location + " -> " + self.destination + "\n" + self.train_route_type
        + "\nAvg. tid: " + self.departure_time.strftime('%Y-%m-%d %H:%M') + "\nAnk. tid: " 
        + self.arrival_time.strftime('%Y-%m-%d %H:%M')
        + "\nTågnummer: " + str(self.train_number) + "\nTågresenummer: " + str(self.train_route_number))
        return repr

# A class that contains a list of train routes to be able to store
# multiple train routes.
#   train_routes - a list of TrainRoute objects
class TrainRouteList:

    def __init__(self, train_routes):
        """Creates a new train route list
        Parameters: self, train_routes (a list of TrainRoute objects)
        Return: nothing"""
        self.train_routes = train_routes

    def __repr__(self):
        """Returns a string representation of the train route list.
        Parameters: self
        Return: repr (string)"""
        repr = ""
        i = 0
        for train_route in self.train_routes:
            i += 1
            repr = repr + str(i) + ".\n" + str(train_route) + "\n\n" 
        return repr

    def find_train_route_number(self, train_route_number):
        """Searches for a train route number.
        Parameters: self, train_route_number (int)
        Return: found_train_route (a train route that matches the searched train route number)"""
        found_train_route = None
        for found_train_route in self.train_routes:
            if found_train_route.train_route_number == train_route_number:
                return found_train_route
        return found_train_route

    def find_train_number(self, train_number):
        """Searches for a train number.
        Parameters: self, train_number (int)
        Return: found_train_route (a train route that matches the searched train route number)"""
        found_train_route = None
        for found_train_route in self.train_routes:
            if found_train_route.train_number == train_number:
                return found_train_route
        return found_train_route

    def get_train_route_by_index(self, index):
        """Searches for a train_route in the list with the given index.
        Parameters: self, index (int)
        Return: train_route (a train route in the list at the given index)"""
        if index < 0 or index > (len(self.train_routes) - 1):
            raise IndexError("The index is out of bounds.")
        else:
            return self.train_routes[index]

    def update(self):
        """Updates the train route list by deleting the train route lists that has passed
        the current time and date.
        Parameters: self
        Return: nothing"""
        for train_route in self.train_routes:
            i = 0
            if train_route.departure_time <= datetime.datetime.now():
                self.train_routes.remove(train_route)
            i += 1

# A class that defines a train
# train_number - int
# name - the name of the train, string
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
        repr = "VAGN " + str(self.train_cart_number) + "\n┏"
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
        Calls function seat.is_available()
        Parameters: self
        Returns: available_seats (int)."""
        available_seats = 0
        for seat in self.seats:
            if seat.is_available():
                available_seats += 1
        return available_seats

    def book_seat(self, seat_number):
        """Book a selected seat. Returns the booked Seat if booking is successful.
        Calls function seat.is_available() and seat.book()
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
        """Cancels a booked seat. Calls function seat.is_available() and seat.cancel()
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

def read_train_file(file_name):
    """Reads from a file with the given file name and creates a new list of train objects.
    Calls function read_seats_from_file(file)
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
    file.close()
    return trains

def write_train_file(file_name, trains):
    """Writes the trains to a file with the fiven file name.
    Calls function write_seats_to_file(file, seats)
    Parameters: file_name (string), trains (a list of Train objects)
    Return: nothing"""
    file = open(file_name, "w")
    for train in trains:
        file.write("Train\n")
        file.write(str(train.train_number) + "\n")
        file.write(str(train.name) + "\n")
        for train_cart in train.train_carts:
            file.write("Cart\n")
            file.write(str(train_cart.train_cart_number) + "\n")
            write_seats_to_file(file, train_cart.seats)
            file.write("\n")
    file.close()
            
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

def read_train_route_file(file_name):
    """Reads from a file and creates a TrainRouteList object from the given input.
    Calls function read_datetime_from_file(file).
    Parameter: file_name (string)
    Return: train_route_list (a TrainRouteList object)"""
    file = open(file_name, "r", encoding="utf-8")
    train_routes = []
    train_route_number = file.readline().strip()
    while train_route_number != "" :
        departure_location = file.readline().strip()
        destination = file.readline().strip()
        train_route_type = file.readline().strip()
        departure_time = read_datetime_from_file(file)
        arrival_time = read_datetime_from_file(file)
        train_number = file.readline().strip()
        price = file.readline().strip()
        train_routes.append(TrainRoute(int(train_route_number), departure_location, destination,
            departure_time, arrival_time, int(train_number), float(price), train_route_type))
        train_route_number = file.readline().strip()
    train_route_list = TrainRouteList(train_routes)
    file.close()
    return train_route_list

def write_train_route_file(file_name, train_route_list):
    """Write the train routes to the train route file. 
    Calls function write_datetime_to_file(file, date_time).
    Parameter: file_name(string), train_route_list (a TrainRouteList object)
    Return: nothing"""
    file = open(file_name, "w", encoding="utf-8")
    for train_route in train_route_list.train_routes:
        file.write(str(train_route.train_route_number) + "\n")
        file.write(train_route.departure_location + "\n")
        file.write(train_route.destination + "\n")
        file.write(train_route.train_route_type + "\n")
        write_datetime_to_file(file, train_route.departure_time)
        write_datetime_to_file(file, train_route.arrival_time)
        file.write(str(train_route.train_number) + "\n")
        file.write(str(train_route.price) + "\n")

def read_datetime_from_file(file):
    """Reads the date and time from file and returns a datetime object.
    Parameters: file (a file)
    Return: datetime (a datetime object)"""
    year = int(file.readline().strip())
    month = int(file.readline().strip())
    day = int(file.readline().strip())
    hour = int(file.readline().strip())
    minute = int(file.readline().strip())
    return datetime.datetime(year, month, day, hour, minute)

def write_datetime_to_file(file, date_time):
    """Writes the date and time to a file.
    Parameters: file (a file), date_time (datetime)
    Return: nothing"""
    file.write(str(date_time.year) + "\n")
    file.write(str(date_time.month) + "\n")
    file.write(str(date_time.day) + "\n")
    file.write(str(date_time.hour) + "\n")
    file.write(str(date_time.minute) + "\n")

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

def book_tickets(number_of_tickets, train, train_route, train_cart):
    """Books the given number of tickets.
    Parameters: number_of_tickets (int), train (a Train object), train_route (a TrainRoute object), train_cart (a TrainCart object)
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
                seat = train_cart.book_seat(int(seat_number))
                if seat == None:
                    print("Ange ett annat platsnummer: ")
                else:
                    tickets.append(Ticket(seat, train_route, train_cart, train))
                    break
            except IndexError:
                print("Vänligen ange ett korrekt platsnummer: ")
            seat_number = input()
        print(train_cart)
    return tickets

def train_ticket_menu(train_route, train):
    """Displays the train ticket menu to the user.
    Parameters: train_route (a TrainRoute object), train (a Train object)
    Return: tickets (a list of Ticket objects)"""

    menu_choices = ("\nVad vill du göra?\nByt vagn, skriv 'V'\nBoka, skriv 'B', på samma rad följt av önskat antal biljetter (exempel B 2).\n" +
        "Avboka, skriv 'A', på samma rad följt av ett platsnummer (exempel A 10).\nGå tillbaka till huvudmeny, skriv 'H'.\n")
    train_cart = train.train_carts[0]
    tickets = []
    print(menu_choices)
    print("Bokade platser markeras med * *")
    print(train_cart)
    user_input = get_input(train_cart)
    
    while user_input != 'H':
        if user_input == 'V':
            train_cart = change_train_cart(train, train_cart)
        elif user_input[0] == 'B':
            tickets = tickets + (book_tickets(int(user_input[2:]), train, train_route, train_cart))
            print("")
        elif user_input[0] == 'A':
            try:
                train_cart.cancel_booked_seat(int(user_input[2:]))
            except IndexError:
                print("Det angivna platsnumret är ogiltigt, försök igen.")
            print("")
        print(menu_choices)
        print(train_cart)
        user_input = get_input(train_cart)
    return tickets

def main_menu(train_route_list, trains):
    """Displays the main menu to the user which offers different choices such as choosing train route and printing tickets.
    Parameters: train_route_list (a TrainRouteList object), trains (a list of Trains)
    Returns: nothing"""
    menu_choices = ("Vad vill du göra?\nVälja tågresa, skriv 'T'\nSkriv ut de senaste bokade biljetterna, skriv 'S'.\nAvsluta, skriv Q.")
    tickets = []
    print(menu_choices)
    user_input = input("Ange ett val: ")
    
    while user_input != 'Q':
        if user_input == 'T':
            tickets = tickets + train_route_choice_menu(train_route_list, trains)
        elif user_input == 'S':
            print_tickets("tickets.txt", tickets)
            print("Biljetterna har skrivits ut till filen 'tickets.txt'.")
        else:
            print("Vänligen ange ett giltigt val.")
        print("\n" + menu_choices)
        user_input = input("Ange ett val: ")

def change_train_cart(train, cart):
    """Returns the next train cart in the list.
    Parameters: train (a Train object), cart (a TrainCart object)
    Return: train_cart (a Train cart object)"""
    number = 0
    if cart.train_cart_number != len(train.train_carts):
        number = cart.train_cart_number
    for train_cart in train.train_carts:
        if train_cart.train_cart_number == number + 1:
            return train_cart

def train_route_choice_menu(train_route_list, trains):
    """Displays a train route choice menu to the user.
    Parameters: train_route_list (TrainRouteList object), trains (a list of Trains)
    Return: tickets (a list of Ticket objects)"""
    tickets = []
    while True:
        print("\nTILLGÄNGLIGA TÅGRESOR: \n" + str(train_route_list))
        user_input = input("Ange numret för vilken tågresa du vill boka eller avboka: ")
        if is_integer(user_input):
            if int(user_input) < 1 or int(user_input) > len(train_route_list.train_routes):
                print("Det angivna värdet måste vara mellan 1 och " + str(len(train_route_list.train_routes)))
            else:
                index = int(user_input) - 1
                train_route = train_route_list.get_train_route_by_index(index)
                train = get_train(trains, train_route.train_number)
                tickets = train_ticket_menu(train_route, train)
                break
        else:
            print("Vänligen ange ett giltigt värde.")
    return tickets

def get_train(trains, train_number):
    """Returns a train that matches the train number from a list of trains.
    Parameters: trains (a list of Train objects), train_number (int)
    Returns: train (a Train object)"""
    for train in trains:
        if train.train_number == train_number:
            return train

def get_input(train):
    """Gets the input from the user and returns the choice.
    Parameters: train (a Train object)
    Return: user_input (string)"""
    while True:
        try:
            user_input = input("Ange ett val: ").capitalize()
            if user_input == 'V' or user_input == 'H':
                break
            elif re.match("^B\s[0-9]+$|^A\s[0-9]+$", user_input):
                if int(user_input[2:]) <= 0 or int(user_input[2:]) > len(train.seats):
                    print("Du måste ange ett nummer mellan 1 och " + str(len(train.seats)) + ". Vänligen ange nytt val.")
                if user_input[0] == 'B' and int(user_input[2:]) > train.number_of_available_seats():
                    print("Du kan inte boka fler platser än de som finns tillgängliga. Vänligen ange nytt val.")
                else:
                    break
            else:
                print("Vänligen ange ett giltigt val som beskrivet ovan.")
        except IndexError or AttributeError:
                print("Vänligen ange ett giltigt val som beskrivet ovan.")
    
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
    """This is the main function of the program.
    The main function
    Algorithm:
    1. Welcome the user.
    2. Read data from the files.
    3. Display all options in a menu.
    4. The user can choose an option or quit the program.
    5. If the user does not choose to quit, they can continue to choose an option
    6. Step 3-5 is repeated until the user quits.
    7. Save data and quit program
    Parameters: none
    Returns: nothing
    """
    print("Välkommen till SJ:s platsbokning.\n")
    trains = read_train_file("trains.txt")
    train_route_list = read_train_route_file("train_routes.txt")
    train_route_list.update()
    main_menu(train_route_list, trains)
    write_train_file("trains.txt", trains)
    write_train_route_file("train_routes.txt", train_route_list)

main()
