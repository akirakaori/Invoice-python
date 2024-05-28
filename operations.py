import write
import datetime


# Function to display a welcome screen with options
def display_welcomescreen():  
     print("+========================================+")
     print("|     Welcome to TechnoPropertyNepal     |")
     print("+========================================+")
     print("| Option |         Action                |")
     print("+========+===============================+")
     print("|   1    |         Rent Land             |")
     print("|   2    |         Return Land           |")
     print("|   3    |         Exit                  |")
     print("+========+===============================+")

     
# Function to display available land information in a tabular format
def lands_display(land_information):
     print("Available land_information")
     print("+======+==============+=====================+======+============+==================+")
     print("|  ID  |     City     |      Direction      | Anna | Price      | Availability     |")
     print("+======+==============+=====================+======+============+==================+")

   # Loop through the list of land information and format each entry
     for land in land_information:
          print("| {:<4} | {:<12} | {:<19} | {:<4} | {:<10} | {:<16} |".format(land['land_id'], land['city'], land['direction'], land['anna'], land['price'], 'Available' if land['available'] else 'Not Available'))
          print("+======+==============+=====================+======+============+==================+")


# Function to handle land rental proces
def rent_land(land_information):
     '''
    this allows a user to rent land. Prompts the user to enter their name and 
    choose a land ID from the available lands. Users can also specify 
    the rental duration and receive an invoice.
    '''
     name = validate_name("Enter your name: ")
     if name is None:
          return
     
     rented_land_information = []# Store information of rented lands
     total_amount = 0   # Initialize total rental cost


     while True:
          # Allow the user to choose an available land ID
          land_id = choose_land_id(land_information, available=True)

          
          # Find the corresponding land object
          land= next((land for land in land_information if land["land_id"] == land_id) , None)
          if land and land["available"]:
               duration = validate_duration("Enter rental duration(month): ")
               if duration == 0:
                    continue #Skip if duration is invalid

               # Calculate rental amount based on land price and duration
               amount = land["price"] * duration
               total_amount += amount   #Update total amount
               rented_land_information.append({"land_id": land_id, "duration": duration, "amount": amount,"city":land["city"], "direction":land["direction"], "anna":land["anna"], "price":land["price"]})
                # Mark the land as no longer available
               land["available"] = False 
          else:
               print("Land is not availble.")   

          # Prompt the user whether to continue renting or exit
          continueornot=input("Do you want to continue or  press Y: ")
          if continueornot=="y":
               continue #Continue the loop if the user wants to rent more lands
          else:
               write.invoice_generation(rented_land_information, land_information, name,total_amount)
               break# Exit the loop and stop renting



# Function to return rented land
def return_land(land_information):
     '''
     Allows a user to return rented land. Prompts the user to enter their name, 
     choose a land ID from the rented lands, and optionally enter a late return duration.
     '''
     name = validate_name("Enter your name: ")# Validate user name
     if name is None:
          return #Exit if the name is not valid
     
     return_land_information =[]
     total_fine = 0

     while True:    
          land_id = choose_land_id(land_information, available=False) 
         
          land = next((land for land in land_information if land["land_id"] == land_id and not land["available"]), None)
          if land:
               late_duration = validate_late_duration("Enter late duration (month): ")
               if late_duration == -1:
                    continue
               fine = land["price"]*late_duration*0.1
               total_fine += fine + land["price"]
               # Store rented land information
               return_land_information.append({"land_id": land_id, "late_duration": late_duration, "fine": fine, "city": land["city"], "direction": land["direction"], "anna": land["anna"], "price": land["price"]})

               land["available"] =True
          else:
              print("Land is avilable or Invalid.") 

          continueornot=input("Do you want to continue or  press y: ")
          if continueornot=="y":
               continue
          else:
               write.return_invoice(return_land_information,land_information, name , total_fine)# Generate invoice when the user decides to stop
               break
           
                    

















def validate_name(prompt):
    while True:
        name = input(prompt)
        has_digit = False
        
        # Check if the name contains any digits
        for char in name:
            if char.isdigit():
                has_digit = True
                break
        
        if has_digit:
            print("Name cannot contain numbers.")
            continue_choice = input("Do you want to try again? (y/n): ").lower()
            if continue_choice != 'y':
                return None
        else:
            return name
        

                 

               

def validate_duration(prompt):
    """
    Validates the rental duration entered by the user.
    The duration must be a positive integer.
    Prompts the user until a valid duration is entered.

    Parameters:
        prompt (str): The message to display when asking for input.

    Returns:
        int: A valid positive integer representing the rental duration.
    """
    while True:
          try:
               duration = int(input(prompt))# Attempt to convert input to an integer
               if duration > 0:
                    return duration  # Return the valid positive duration 
               else:
                    print("Duration must be a positive number.")

          except ValueError:
               print("Invalid input. Please enter a valid number.")# Error message for non-integer input


def validate_late_duration(prompt):
     """
     Validates the late duration entered by the user.
     The late duration must be a non-negative integer.
     Prompts the user until a valid late duration is entered.

     Parameters:
          prompt (str): The message to display when asking for input.

     Returns:
          int: A valid non-negative integer representing the late duration.
     """
     while True:
          late_duration_str = input(prompt)# Get input as a string
          try:
               late_duration = int(late_duration_str) # Attempt to convert input to an integer
               if late_duration >= 0:
                    return late_duration # Return the valid non-negative late duration
               else:
                    print("Late duration must be a non-neagtive number.") # Error message for negative late duration
          except ValueError:
               if late_duration_str.isdigit():  # If input has digits but is invalid
                    print("Late duration must be a non negative number.")# Specific message for non-negative requirement
               else:
                    print("Invalid input. PLease enter a valid number.")  # General error message for invalid input


def choose_land_id(land_information, available=True):
    while True:
        try:
            land_id = int(input("Enter land ID (Press 0): "))  #something is missing 
            if land_id == 0:
                return 0

            valid_land = False
            for land in land_information:
                if land["land_id"] == land_id and land["available"] == available:
                    valid_land = True
                    break
            
            if valid_land:
                return land_id
            else:
                print("Invalid land ID.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def choose_option():
     while True:
          try:
               option = int(input("Enter your choice: "))
               if option in [1, 2, 3]:
                    return option 
               else:
                    print("Option not avilable")

          except ValueError:
               print("Invalid input. PLease enter a valid number.")


def validate_land_data(data):
     """
     Validates the land data to ensure it has the correct format and valid values.

     Parameters:
          data (list): A list of land data elements.

     Returns:
          bool: True if the data is valid, False otherwise.
     """
     if len(data) !=6:
          print("Invalid land data format.")
          return False
     try:
          int(data[0]) #land_id
          data[1]     #city
          data[2]     #direction
          int(data[3])#Anna
          int(data[4])#price
          available_status = data[5].lower()# Check if availability status is either "available" or "not available"
          if available_status.startswith('available') or available_status.startswith('not available'):
               return True
          else:
               print("Invalid availability status.")# Error message for invalid availability status
               return False
     except ValueError:
          print("Invalid land data values.")  # Error message for invalid value types
          return False
               
          
                         


          

