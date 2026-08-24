def get_driver_name():
    # Keep prompting user until a valid input is made
    while True:
        # .strip() removes accidental leading and trailing whitespace
        name = input("Enter full name of driver: ").strip()

        # Test whether there is no name
        if name != "":
            return name

        print("Driver name cannot be empty.")


def get_licence_number():
    # Get the licence number
    while True:
        licence = input("Enter licence number: ").strip()

        # Licence must be 8 characters:
        # first 2 must be letters and last 6 must be numbers
        if (len(licence) == 8 and
                licence[:2].isalpha() and
                licence[2:].isdigit()):
            return licence.upper()  # Normalize licence to uppercase

        print("Licence number invalid (needs 2 letters followed by 6 numbers).")


def get_posted_speed():
    # Get the speed limit
    while True:
        try:
            speed = int(input("Enter posted speed (km/h): "))

            # Speed limit should be between 30 and 110
            if 30 <= speed <= 110:
                return speed

            print("Posted speed must be between 30 and 110 km/h.")

        # Ensures the program does not crash on non-integer input
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


def check_wanted(driver_name, wanted_list):
    # Checks the wanted list using stripped, lower-case comparison
    clean_driver_name = driver_name.strip().lower()

    for wanted_name in wanted_list:
        if clean_driver_name == wanted_name.strip().lower():
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
    print("Fine: $" + str(fine))

    # Check whether the driver is on the wanted list
    if check_wanted(name, wanted_list):
        print("WARNING: This driver is on the wanted list!")


def view_recorded_offences(offences):
    #views all offences that have been recorded so far
    print("View Recorded Offences")

    if len(offences) == 0:
        print("No speeding offences have been recorded.")
        #if no speeding offences were recorded
        return

    print("Driver       Licence     Limit   Speed   Over    Fine")
    print("=" * 64)

    # Display every recorded offence
    for offence in offences:
        print(offence["name"],
              offence["licence"],
              offence["posted"],
              offence["speed"],
              offence["over"],
              "$" + str(offence["fine"]))


def search_driver(offences):
    # Search for a driver using their name or licence number
    print("Search Driver")
    print("1. Search by driver name")
    print("2. Search by licence number")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        #asks for the name and removes space and uppercase
        search_name = input("Enter driver name: ").strip().lower()

        found = False
        total_fines = 0

        print("Driver Offences")
        print("=" * 64)

        # Check every offence for a matching name
        for offence in offences:
            if offence["name"].strip().lower() == search_name:
                #if it is found
                found = True

                print("Driver:", offence["name"])
                print("Licence:", offence["licence"])
                print("Posted speed:", offence["posted"], "km/h")
                print("Recorded speed:", offence["speed"], "km/h")
                print("Over limit:", offence["over"], "km/h")
                print("Fine: $" + str(offence["fine"]))
                print("-" * 64)

                total_fines += offence["fine"]

        if found:
            print("Total fines for this driver: $" + str(total_fines))
        else:
            print("No offences found for this driver.")
            #checks if there are any offences found within the driver name

    elif choice == "2":
        search_licence = input("Enter licence number: ").strip().lower()

        found = False
        total_fines = 0

        print("Driver Offences")
        print("=" * 64)

        # Check every offence for a matching licence
        for offence in offences:
            if offence["licence"].strip().lower() == search_licence:
                #when it's found
                found = True

                print("Driver:", offence["name"])
                print("Licence:", offence["licence"])
                print("Posted speed:", offence["posted"], "km/h")
                print("Recorded speed:", offence["speed"], "km/h")
                print("Over limit:", offence["over"], "km/h")
                print("Fine: $" + str(offence["fine"]))
                print("-" * 64)

                total_fines += offence["fine"]

        if found:
            print("Total fines for this driver: $" + str(total_fines))
        else:
            print("No offences found for this licence number.")

    else:
        print("Invalid choice.")
        #checks if there are any offences found within the lisense number


def patrol_summary(offences):
    print("Patrol Summary")

    if len(offences) == 0:
        print("No speeding offences have been recorded.")
        return

    total_fines = 0
    total_over = 0

    # Start with the first offence as the highest
    highest_offence = offences[0]

    # Go through every recorded offence
    for offence in offences:
        total_fines += offence["fine"]
        total_over += offence["over"]

        # Find the offence with the highest speed over the limit
        if offence["over"] > highest_offence["over"]:
            highest_offence = offence

    # Calculate average speed over the limit
    average_over = total_over / len(offences)
    #length of the dictionary to check amount in the list (How many offences)
    print("Amount of offences:", len(offences))
    print("Total fines issued: $" + str(total_fines))
    print("Average speed over limit:",
          round(average_over, 1), "km/h")

    print("Highest offence:")
    #Calls highest offence function
    print("Driver:", highest_offence["name"])
    print("Over limit:", highest_offence["over"], "km/h")


def display_menu():
    #Displays the options for menu
    print("Main Menu")
    print("1. Record a speeding offence")
    print("2. View all recorded offences")
    print("3. Display patrol summary")
    print("4. Search driver")
    print("5. Exit")


def main():
    # List used to store all recorded offences
    offences = []

    # List of wanted people
    wanted_list = [
        "John Smith",
        "May Jones",
        "Peter Brown",
        "Jack Wilson",
        "Sarah Taylor",
        "Liam Anderson",
        "Olivia Martin",
        "Noah Thompson"
    ]

    # Keep displaying the menu until the user chooses to exit
    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()
        #Calls function of whatever was chosen

        if choice == "1":
            record_offence(offences, wanted_list)

        elif choice == "2":
            view_recorded_offences(offences)

        elif choice == "3":
            patrol_summary(offences)

        elif choice == "4":
            search_driver(offences)

        elif choice == "5":
            print("Exiting program")
            break
            #ends program

        else:
            print("Invalid choice. Please select 1 to 5.")


main()
#calls the main function




