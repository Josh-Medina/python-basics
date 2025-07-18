## Section Lookup Script – Pseudocode ##

1. "What section would you like to view?"
1. Accept user input for a section title (EX: "VARIABLES")
1. Store that input in a variable (EX: target_section)

### Open the markdown file in read mode ###

1. open file with open(filename, "r") as file:
2. read the file line by line in the section specified

#### For each line in the file: ####

1. if line starts with '#' and contains the user input in variable target_section:
1. print out the section bieng referenced

#### If no match is found for section ####

1. print "Section not found."
1. Use a while loop to offer the user to try again or exit