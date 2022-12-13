#This program is to identify the age based on the birth year of a users.


name=input("Enter your name please? ")   # He/she will input the Name.
print(name,  "Hi Thank you!")
input("How are you today: ")

print("That's great!")

from datetime import date              # Import date is the package on python to give support as function.
date_of_birth = int(input("In which year you took birth: "))

today_date = date.today().strftime("%Y") # Formula for calculation of age according to the birth year.

print("Your current age is ",int(today_date)-date_of_birth)
print("Thank you , Have a good day!")

#END...................................