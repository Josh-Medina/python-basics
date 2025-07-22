# defining the get_letter_grade function that converts
# a numeric score to a letter grade

def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Defining a function to validate the user's score input

def get_valid_score():
    while True:  # Keep asking until the valid input is recieved
        try:
                # Prompt the user, remove spaces, and try converting to float
            score = float(input("Enter score (0-100): ").strip())
            if 0 <= score <= 100:  
                return score  # if the score is in the valid range, return it
            else:
                print("Score must be between 0 and 100.") # print error message if score entered isnt in valid range
        except ValueError:     
            print("Invalid input. Please enter a numeric score.") # If user enters strange characters it prompts them accordingly


#  This function prints each student's name, score,
#  and letter grade to the student summary

def print_summary(student_list):
    print("\nStudent Summary:")
    for name, score, grade in student_list: # Loop through each student record (a tuple of name, score, grade)
        print(f"{name}: {score} -> {grade}")  # Print in the format: Name: Score -> Grade

# Function to save student data to a file called grades.txt
def save_to_file(student_list):
    with open("grades.txt", "w") as file:
        for name, score, grade in student_list:
            file.write(f"{name}: {score} -> {grade}\n")


# Function to get a yes/no answer from the user & validate the response
        
def get_yes_or_no(prompt):
    while True:   # Keep asking until the input is either 'yes' or 'no'
        response = input(prompt).strip().lower()
        if response == "yes":
            return True   # User wants to continue
        elif response == "no":
            return False # User wants to stop
        else:    # Invalid input - keep prompting
            print("Invalid input, please type 'yes' or 'no'")
                  
# Main program

# Print the welcome message
print("Welcome to the student Grade Tracker!")

# Empty list to store student data

students = []

# Begin the main loop & continue till user says no

while True:
      name = input("Enter student name: ").strip().title()
      score = get_valid_score()
      grade = get_letter_grade(score)
      students.append((name, score, grade))

      if not get_yes_or_no("Add another student? (yes/no):"):
                           break

print_summary(students) # print a summary of all students
save_to_file(students)  # save all data to a file
print("Student data saved to grades.txt")  # confirmation that the file has been saved.






