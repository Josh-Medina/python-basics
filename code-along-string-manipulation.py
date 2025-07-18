string1 = 'This is a valid string'
string2 = "This is also a valid string"
string3 = "This is NOT a valid string - see why?"

palindrome = "Go hand a salami, I'm a lasagna hog"

# Using a quote inside string

string3 = "'Always look on the bright side of life' - Monty Python"

# Use escape character to include quotes in string

string4 = "\"Always look on the bright side of life\" - Monty Python"
print(string4)

print(len(string4))

name = "      Josh  "
print(len(name))
print(name)
print("Hello" + name)

name_no_spaces = name.strip()
print(len(name_no_spaces))
print(name_no_spaces)
print("Hello " + name_no_spaces)

# split()

filepath = "/var/josh/here"
folders = filepath.split("/")
print(folders)
print(type(folders))