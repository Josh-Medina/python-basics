# VARIABLES #

## Description:## 
Used to store date values of different types( text, numbers, true/false)

 name = "Alice"     # string 
age = 25            # integer
height = 5.6        # float 
is_student = True   # Boolean 

## Useful for: ##
 storing user data, configuring app settings, temporary values in logic.


# INPUT & OUTPUT #

## Description: ##  
input() gets information from the user, print() shows/displays the data to the user

name = input("Enter your name: ") 
print("Hello, " + name)

## Useful for: ##
programs needing information from user & tools used from the CLI.


# TYPE CONVERSION #
## Description: ##
Converts one data type to another ( string to an int, float, bool, etc)

Python
 age = int(input("Enter your age: "))   # Convert string to int
height = float(input("Enter height: ")) # Convert string to float 
commonly used this way) # Convert string to bool (not commonly used this way)

## Useful For: ##
Ensuring correct types of data for math operations or logic checks.


# LISTS #
## Description: ## 
Stores multiple values in a single variable. Lists are ordered and you can change them. Indexed starting at [0]

fruits = ["apple", "banana", "cherry"]  # list of items called "fruits"
print(fruits[0])   # Access the item at index [0]
fruits.append("grape")  # Add item "grape at the end of the list
fruits.remove("banana")  # Remove item "banana" from list
print(len(fruits)) # list the length

## Useful For: ##
Collections of items, for & while loops, data processing, etc.


# IF STATEMENTS #
## Description: ##
Will run a different piece of code depending on a condition, allows you to use multiple if statements together.

age = 18  
if age >= 18:  
    print("You're an adult")  
elif age > 12:  
    print("You're a teenager")  
else:  
    print("You're a child")

## Useful For: ##
Helful with decision-making logic like menus, access control, branching logic.


#  FOR LOOPS #
## Description: ##
Description:
Repeats a block of code for each item in a list or a range.

fruits = ['apple', 'orange', 'banana']  
for fruit in fruits:  
    print(fruit)

## Useful For: ##
Going through lists, processing data, printing things.


# WHILE LOOPS #
## Description: ##
Keeps looping going while a condition is true.

count = 0  
while count < 3:  
    print("Count is", count)  
    count += 1

guess = 0  
while guess != 7:  
    guess = int(input("Guess the number: "))  

## Useful For: ##
Repeating something an unknown number of times, user input loops, retry logic for mistaken input, etc.


#  FUNCTIONS #
## Description: ##
Reusable blocks of code with optional input and output. Very helpful for shortening amount of code needing to be written.

def greet(name):  
    print("Hello, " + name)

greet("Alice")


def add(a, b):  # Function with a return
    return a + b

## Useful For: ##
Organizing code, avoiding repetition, modular programming.


# FILE I/O – WRITE #
## Description ##
Creates a file or overwrites if it exists.

with open("example.txt", "w") as file:  
    file.write("Hello, world!\n")

## Useful For: ##
Storing logs, saving user data, exporting results.


# FILE I/O – READ #
## Description ##
Reads the contents of a file.

with open("example.txt", "r") as file:  
    contents = file.read()  
    print(contents)

## Useful For: ##
Reading configation files, loading saved data, etc.


# FILE I/O – APPEND #
## Description ##
Adds new content to the end of the file without deleting existing content.

with open("example.txt", "a") as file:  
    file.write("Adding another line.\n")

## Useful For: ##
Logs, journals, growing datasets.


# FILE I/O – READ LINE BY LINE
## Description ##
Go through each line one at a time, strip() removes newline characters.

with open("example.txt", "r") as file:  
    for line in file:  
        print(line.strip())

## Useful For: ##
Going through large files, parsing  out line-by-line data,  or processing logs.