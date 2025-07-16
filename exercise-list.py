# Play with for loops

# Create a list

# Use a for loop to iterate
# through the list

# input clients name:

name = input("What is your name?:")

# space for readability

print()

print(f"Welcome to your chest day training program, {name}!")

print()

#Creating exercise list

exercise_list = ["Flat barbell bench press", "Incline dumbell bench press", "Chest dips", "Cable fly",]
print("Perform your exercises in this list:", exercise_list)

# Print a blank line for readability
print()

# list for sets & reps
sets_reps = ["4 sets, 6 reps",
             "4 sets, 8 reps",
             "3 sets, 10 reps",
             "3 sets, 15 reps"]

# loop through exercises & reps together

for i in range(len(exercise_list)):
               print(f"{i+1}. {sets_reps[i]}: {exercise_list[i]}")
               

print()

# Mark an exercise as done

done_task = exercise_list.pop(0),sets_reps.pop(0)
print("You completed:", done_task)
print()
print("Exercises left, don't be lazy!:")

print()

for i in range(len(exercise_list)):
        print(f"-{exercise_list[i]} ({sets_reps[i]})")




