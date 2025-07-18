file_path = 'data.csv'

'''print(file_path)

file = open(file_path, 'r')
file = open(file_path, 'w')
file = open(file_path, 'a')
file = open(file_path, 'r+')

# write function will create a new file or overwrite an existing one
file = open('example2.txt', 'w')
file.write("Hello, World!\n")
file.write("This is line two!\n")
file.close()

# open a fie using the "with" keyword

with open("example-with.txt", "w") as file:
    file.write("We wrote this file using the 'with' keyword!\n")
    file.write("this is line 2 \n")
    file.write("This is line 3\n")

# read function to read the contents of a file

with open("example-with.txt", "r") as file:
    contents = file.read()
    print(contents)

    # Use a for loop to read lines from a file

    with open("example-with.txt", "r") as file:
        for line in file:
            print(line.strip())'''

# Append to a file using with

with open("example-with.txt", "a") as file:
    file.write("This is an appended line!\n")