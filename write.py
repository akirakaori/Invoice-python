import datetime

#Function to update land information in a file
def update_land_information_in_file(land_information):
    try:
        # Open file in append mode to avoid overwriting existing data
        # To preserve existing data, use 'a' for append mode.
        with open("landdata/land_information.txt", "w") as file:
             # Iterate through each land item and write its details to the file
            for land in land_information:
                 # Convert necessary data to strings
                land_id_str = str(land['land_id'])
                city_str = land['city']   
                direction_str = land['direction']  
                anna_str = str(land['anna'])
                price_str = str(land['price'])
                available_str = "Available" if land['available'] else "Not Available"

                 # Format and write the land information to the file
                file.write(f"{land_id_str}, {city_str}, {direction_str}, {anna_str}, {price_str}, {available_str}\n")
    except (IOError, FileNotFoundError) as e: 
        # Handle exceptions related to file operations
        print("Error occurred while writing land data:", e)


# Function to generate a timestamp
def generate_timestamp():
    """
    Generates a timestamp in the format 'YYYYMMDDHHMMSS'.

    Returns:
        str: The generated timestamp.
    """
    # Get the current date and time
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    return timestamp



def invoice_generation(rented_land_information,land_information,name, total_amount):
    """
    Generates an invoice for rented land.

   
        rented_land_information (list of dict): List containing information about rented land.
        land_information (list of dict): List containing updated land information.
        name (str): The name of the renter.
        total_amount (float): The total amount to be paid for renting.
    """
    if rented_land_information:
                    # Update the land information file with the latest data
                    update_land_information_in_file(land_information)    # Generate a timestamp for unique invoice naming              
                    timestamp = generate_timestamp()
                    now =datetime.datetime.now()

                    formatted_date_time = now.strftime("%Y/%m/%d %H:%M:%S")
                             # Define the invoice name using renter's name and timestamp
                    invoice_name = "{name}_rent_invoice_{timestamp}.txt".format(name=name, timestamp=timestamp)
                    with open(invoice_name, "w") as file:
                        # Open a new file to write the rental invoice
                         file.write("+------------------------------------------------------------------------------------+\n")
                         file.write("|                               TechnoRentalNepal                                    |\n")
                         file.write("+------------------------------------------------------------------------------------+\n")
                         file.write("|                                                                                    |\n")
                         file.write("|Rent Invoice for {name:<67}|\n".format(name=name))
                         file.write("|Date: {formatted_date_time:<78}|\n".format(formatted_date_time=formatted_date_time))
                         file.write("+------+--------------+---------------------+------+-----------+----------+----------+\n")
                         file.write("|  SN  |     ID       |        City         | Anna | Price     | Duration | Amount   |\n")
                         file.write("+------+--------------+---------------------+------+-----------+----------+----------+\n")
                          # Write details for each rented land item
                         sn = 1
                         print(rented_land_information)
                         for rented_land in rented_land_information:
                              file.write("| {:<4} | {:<12} | {:<19} | {:<4} | {:<9} | {:<8} | {:<8} |\n".format(sn, rented_land['land_id'], rented_land['city'], rented_land['anna'], rented_land['price'], rented_land['duration'], rented_land['amount']))
                              sn += 1
                        # Write the total amount section and end of the invoice
                         file.write("+------+--------------+---------------------+------+-----------+----------+----------+\n")
                         file.write("|                                                                                    |\n")
                         file.write("|Total Amount: {total_amount:<70}|\n".format(total_amount=total_amount))
                         file.write("+------------------------------------------------------------------------------------+\n")
                    print("Invoice created:" +invoice_name)
                    print("\nInvoice:\n")
                     # Read the created invoice and print its content to the console
                    with open(invoice_name, "r")as file:
                         print(file.read())
    else:
                    print("No lands rented.")   



       

def return_invoice(return_land_information, land_information, name, total_fine):
    """
    Generates an invoice for returning rented land, including late fees.

    return_land_information (list of dict): List containing information about returned land.
    land_information (list of dict): List containing updated land information.
    name (str): The name of the renter.
    total_fine (float): The total fine for late returns.
    """
    if return_land_information:
        update_land_information_in_file(land_information)  # Update the land information file with the latest data              
        timestamp = generate_timestamp()
        now = datetime.datetime.now()
        formatted_date_time = now.strftime("%Y/%m/%d %H:%M:%S")

        invoice_name = "{name}_return_invoice_{timestamp}.txt".format(name=name, timestamp=timestamp)
        with open(invoice_name, "w") as file:
            file.write("+----------------------------------------------------------------------------------------+\n")
            file.write("|                                 TechnoRentalNepal                                      |\n")
            file.write("+----------------------------------------------------------------------------------------+\n")
            file.write("|                                                                                        |\n")
            file.write("|Return Invoice for {name:<69}|\n".format(name=name))  
            file.write("|Date: {formatted_date_time:<82}|\n".format(formatted_date_time=formatted_date_time)) 
            file.write("|                                                                                        |\n")
            file.write("+------+--------------+---------------------+------+----------+---------------+----------+\n")
            file.write("|  SN  |     ID       |        City         | Anna | Price    | Late Duration |   Fine   |\n")
            file.write("+------+--------------+---------------------+------+----------+---------------+----------+\n")
            sn = 1
            for returned_land in return_land_information:
                file.write("| {:<4} | {:<12} | {:<19} | {:<4} | {:<8} | {:<13} | {:<8} |\n".format(sn,returned_land['land_id'],returned_land['city'],returned_land['anna'],returned_land['price'],returned_land['late_duration'],returned_land['fine']))
                    
                
                sn += 1
            file.write("+------+--------------+---------------------+------+----------+---------------+----------+\n")
            file.write("|                                                                                        |\n")
            file.write("|Total Fine: {total_fine:<76}|\n".format(total_fine=total_fine))  
            file.write("+----------------------------------------------------------------------------------------+\n")

        print("Invoice created: " + invoice_name)
        print("\nInvoice\n")
        # Read and print the created return invoice to the console
        with open(invoice_name, "r") as file:
            print(file.read())
    else:
        print("No lands returned.")
