# Name: Maria Halvarsson
# Date: 2021-01-21
# Course code: DD100N
# The purpose of this program is to present myself (Maria),
# by printing out text to the user.

FIRST_NAME = "Maria"
CAT_NAME = "Ozzi"
cat_age = 2.5
age = 22
sister_age = 20
dad_age = 60
mom_age = 49

print("Hello, my name is", FIRST_NAME + ". I am", age, "years old.")
print("I have a cat named", CAT_NAME, "and he is", cat_age, "years old.")
print("I have a sister that is", sister_age, "years old, my dad is", dad_age, "and my mom is", str(mom_age) + ".")

average_age = (cat_age +  age + sister_age + dad_age + mom_age)/5
age_in_hours = 22 * 365 * 24 + 6 * 24

print("The average age in my family, including my cat, is", average_age, "years.")
print("My age,", "which is", str(age) + ", equals", age_in_hours, "hours (including leap years).")