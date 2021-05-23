# Name: Maria Halvarsson
# Date: 2021-03-01
# Course code: DD100N7
# This program allows the user to save the long jump results of 3 students,
# where each student jumps 3 times. After entering all the necessary data,
# the user can choose between different menu choices:
# 1. Show all results, 2. Show the longest jump for each student, 
# 3. Show the length of the last jump and 4. Quit program.
# The constants NUMBER_OF_STUDENTS and NUMBER_OF_JUMPS can be modified for
# a different number of students and/or jumps.

NUMBER_OF_STUDENTS = 3
NUMBER_OF_JUMPS = 3

print("Welcome to the long jump result organizer!")
print("The program assumes that there are", NUMBER_OF_STUDENTS, "students and each student jumps", NUMBER_OF_JUMPS, "times each.")
print("Start by entering the student's name and the length of their jumps.")

long_jump_results = {}
i = 0
while i < NUMBER_OF_STUDENTS:
    student_name = input("Name of the student: ")

    jump_lengths = []
    j = 0
    while j < 3:
        jump_lengths.append(float(input("Enter the length of jump number " + str(j + 1) + ": ")))
        j += 1
    long_jump_results[student_name] = jump_lengths

    i += 1

choice = '0'
while choice == '0':
    print("1. Show all results")
    print("2. Show the longest jump for each student")
    print("3. Show how long the last jump was for each student")
    print("4. Quit program")
    choice = input("Please choose a number between 1-4: ")

    if choice == '1':
        print("-- ALL RESULTS --")
        for name in long_jump_results.keys():
            print("Name:", name)
            i = 1
            for result in long_jump_results[name]:
                print("Jump " + str(i) + ":", result, "meters")
                i += 1
            print("")
        choice = '0'

    elif choice == '2':
        print("-- LONGEST JUMP --")
        for name in long_jump_results.keys():
            print(name + "'s longest jump:", max(long_jump_results[name]), "meters")
        print("")
        choice = '0'

    elif choice == '3':
        print("-- LAST JUMP --")
        for name in long_jump_results.keys():
            print(name + "'s last jump:", long_jump_results[name][NUMBER_OF_JUMPS - 1], "meters")
        print("")
        choice = '0'

    elif choice == '4':
        print("Program closed\n")
        break

    else:
        print("Please enter a valid number\n")
        choice = '0' 
