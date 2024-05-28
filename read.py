
def read_land_information(filename):
    # Reads land information from the file
    land_information = []
    try:
        with open(filename, "r") as file:
            for line in file:
                # Strip extra whitespace and split data by commas
                data = line.strip().split(',')     #convert the first item to an integer
                # Data extraction
                land_id = int(data[0].strip())     # Convert to float
                city = data[1].strip()             # The city name (string)
                direction = data[2].strip()          # The direction (string)
                anna = float(data[3].strip())       # Convert to float
                price = float(data[4].strip())      # Convert to float
                available_status = data[5].strip().lower() #Lowercase for consistency

                # Creating a dictionary for each land record
                land = {
                    "land_id": land_id,
                    "city": city,
                    "direction": direction,
                    "anna": anna,
                    "price": price,
                    "available": available_status == "available"
                }
                # Append to the land_information list
                land_information.append(land)
    except FileNotFoundError:
        print("Error: file not found.")
        return None  
    return land_information         #Return the processed list of land information
         
