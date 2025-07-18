"""our_number = 42

is_guessed = False


# The while loop
while is_guessed == False:

    # Get input from the user

    guess = int(input("Enter your guess"))

    # If statement - Conditional statement to check the guess

    if guess == our_number:
        print("Hooray!")
        is_guessed = True

    elif guess > our_number:
        print("To high!")

    else:
        print("Too low!")

    # stop light

    color = 'Red'

    if color =='Red':
        print("stop!")

    else:
        print('Go!')

        """

"""counter = 1

while counter < 20:
    if counter % 3 == 0 and counter % 5 == 0:
        print(f'{counter}: Fizzbuzz')
        break

    elif counter % 3 == 0:
        print(f'{counter}: fizzbuzz')
    elif counter % 5 == 0:
        print(f'{counter} fizzbuzz')



    counter += 1
"""

# For loop example

loop_range = range(1, 11)
for i in loop_range:
    print(f'Iteration {i}')

print(max(loop_range))

# For loop with a list

fruits = ['apple', 'banana', 'cherry']

for s in fruits:
    print(f'fruit: {s}')

favorite_movies = ['Interstellar','Pain and Gain', 'Midsommer']

for i in favorite_movies:
    print(f'Favorite movies: {i}')

jobs = ['medical' ,'dentist', 'law' , 'cashier', 'truck driver']

for s in jobs:
    print(f'career choices: {s}')
