# Exercise for functions

# Define the traffic light functions & the message they display

def red_light():
    print("Stop! The light is red.")

def yellow_light():
    print("Caution! The light is yellow")

def green_light():
    print("Go! The light is green")


# Define traffic light state function - 
# Ask for user input about traffic light state - 
# then call the appropriate traffice light function
# which will display the statement to the user.

def traffic_light():
    state = input("Is the light red, yellow, or green?")

    if state == "red":
        red_light()
    elif state == "yellow":
        yellow_light()
    elif state == "green":
        green_light()

    else:
        print("Invalid input, choose from options given!")
        traffic_light()


# call the traffic light function to set the progam into action

traffic_light()
