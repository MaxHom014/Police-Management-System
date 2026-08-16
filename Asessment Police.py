def get_driver_name():
    # Keep prompting user until an entry has been made
    while True:
        name = input("Enter full name of driver: ")

        # Test whether there is no name
        if name != "":
            return name

        print("Driver name cannot be empty.")


def get_licence_number():
    # get the licence number
    while True:
        licence = input("Enter licence number: ")

        # Licence number should be 8 characters
        if len(licence) == 8:
            return licence

        print("Licence number invalid (needs 8 characters).")


def get_posted_speed():
    # Get the speed limit
    while True:
        try:
            speed = int(input("Enter posted speed (km/h): "))

            # Speed limit should be between 30 and 110
            if 30 <= speed <= 110:
                return speed

            print("Posted speed must be between 30 and 110 km/h.")

        # Ensures the program does not crash
        except ValueError:
            print("Please enter an integer number.")
    
def get_recorded_speed(posted_speed):
    # Get the recorded speed
    while True:
        try:
            speed = int(input("Enter recorded speed (km/h): "))
            #checks that the recorded speed is over the speed limit
            if speed > posted_speed:
                return speed

            print("Recorded speed must be greater than the posted speed.")
        #validates the speed entered
        except ValueError:
            print("Please enter a whole number.")
            

def calculate_fine(posted_speed, recorded_speed):
    #Calculates how much is owed in fines
    over = recorded_speed - posted_speed

    if over <= 10:
        return 30
    elif over <= 20:
        return 80
    elif over <= 30:
        return 170
    elif over <= 40:
        return 400
    else:
        return 630
    #A loop that tests wether or not the speed was over by a certain amount to calculate fine





            
get_driver_name()
get_licence_number()
posted_speed = get_posted_speed()
recorded_speed = get_recorded_speed(posted_speed)
calculate_fine(recorded_speed, posted_speed)
            
