
# open up the entire quick reference doc #

with open("quick-reference-python-basics.md", "r") as file:
    contents = file.read()

print(contents)

# Go line by line in the quick reference doc

'''with open("quick-reference-python-basics.md", "r") as file:
    for line in file:
        input()  # Wait for Enter key
        print(line.strip())'''

