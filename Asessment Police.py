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

        print("Licence number invalid.")


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