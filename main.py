import read 
import operations


def main():
    """
    Main function to drive the land rental system.
    It reads land information and provides a menu to the user with the following choices:
    1. Rent land
    2. Return rented land
    3. Exit the program
    """
    # Read land information from a specified file
    land_information =read.read_land_information("landdata/land_information.txt")
    while True:
        operations.display_welcomescreen()
        choice = input("Enter your choice:")
        # Perform operations based on user choice
        if choice == '1':
            print("rent")
            operations.lands_display(land_information) # Display available lands
            operations.rent_land(land_information)      # Allow the user to rent land

        elif choice == '2':
             print("return rent")
             operations.lands_display(land_information) # Display available lands
             operations.return_land(land_information)   # Allow the user to return rented land
        
        elif choice == '3':
            # Exit the program if the user chooses to
            print("Existing program....")
            break
        else:
            # basically handle invalid input
            print("Invalid choice! Please enter a valid choice to proceed.")

# Run the main function to start the program
main()












