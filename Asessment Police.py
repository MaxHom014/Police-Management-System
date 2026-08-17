def get_driver_name():
    # Keep prompting user until an entry has been made
    while True:
        name = input("Enter full name of driver: ")

        # Test whether there is no name
        if name != "":
            return name

        print("Driver name cannot be empty.")


def get_licence_number():
    # Get the licence number
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

            # Checks that the recorded speed is over the speed limit
            if speed > posted_speed:
                return speed

            print("Recorded speed must be greater than the posted speed.")

        # Validates the speed entered
        except ValueError:
            print("Please enter a whole number.")


def calculate_fine(posted_speed, recorded_speed):
    # Calculates how much is owed in fines
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

    # Tests how far over the speed limit the driver was
    # to calculate the correct fine


def check_wanted(driver_name, wanted_list):
    # Checks the wanted list to find if the driver is on it
    for wanted_name in wanted_list:
        if driver_name.lower() == wanted_name.lower():
            return True

    return False


def record_offence(offences, wanted_list):
    # Gets all the information needed to record the offence
    print("Record a Speeding Offence")

    name = get_driver_name()
    licence = get_licence_number()
    posted_speed = get_posted_speed()
    recorded_speed = get_recorded_speed(posted_speed)

    over = recorded_speed - posted_speed
    fine = calculate_fine(posted_speed, recorded_speed)

    # Store all information about the offence in a dictionary
    offence = {
        "name": name,
        "licence": licence,
        "posted": posted_speed,
        "speed": recorded_speed,
        "over": over,
        "fine": fine
    }

    # Add the offence to the list of recorded offences
    offences.append(offence)

    print("Offence recorded.")
    print("Fine: $" + (fine))

    # Check whether the driver is on the wanted list
    if check_wanted(name, wanted_list):
        print("WARNING: This driver is on the wanted list!")

def view_recorded_offences(offences):
    # View the recorded offences from the main menu and shows list
    print("View Recorded Offences")

    if len(offences) == 0:
        #In case there isn't any on the list 
        print("No speeding offences have been recorded.")
        return

    print("Driver     Licence     Limit   Speed   Over    Fine")
    print("=" * 64)

    # Display every recorded offence
    for offence in offences:
        print(offence["name"],
              offence["licence"],
              offence["posted"],
              offence["speed"],
              offence["over"],
              "$" + str(offence["fine"]))

