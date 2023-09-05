import requests
import json

def display_banner():
    banner = """
#     #                                    ######                             
##    # #    # #    # #####  ###### #####  #     # #        ##   ##### ###### 
# #   # #    # ##  ## #    # #      #    # #     # #       #  #    #   #      
#  #  # #    # # ## # #####  #####  #    # ######  #      #    #   #   #####  
#   # # #    # #    # #    # #      #####  #       #      ######   #   #      
#    ## #    # #    # #    # #      #   #  #       #      #    #   #   #      
#     #  ####  #    # #####  ###### #    # #       ###### #    #   #   ###### 
                                                                              
#     #                                    #     #                      
##    # #    # #    # #####  ###### #####  #  #  #   ##   #    #  ####  
# #   # #    # ##  ## #    # #      #    # #  #  #  #  #  ##   # #    # 
#  #  # #    # # ## # #####  #####  #    # #  #  # #    # # #  # #      
#   # # #    # #    # #    # #      #####  #  #  # ###### #  # # #  ### 
#    ## #    # #    # #    # #      #   #  #  #  # #    # #   ## #    # 
#     #  ####  #    # #####  ###### #    #  ## ##  #    # #    #  ####  
    """
    print(banner)

def query_dvla(registration_number, api_key):
    # API endpoint
    api_url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
    
    # Headers for the API request
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }
    
    # Request body
    payload = {
        "registrationNumber": registration_number
    }
    
    # Make the API request
    response = requests.post(api_url, headers=headers, json=payload)
    
    # Check the response
    if response.status_code == 200:
        # Parse the JSON response
        vehicle_info = json.loads(response.text)
        
        # Display the vehicle information
        print("Vehicle Information:")
        for key, value in vehicle_info.items():
            print(f"{key}: {value}")
    else:
        print(f"Failed to retrieve information. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":

    display_banner()  # Call the function to display the banner
    
    # User input for vehicle registration number
    registration_number = input("Enter the vehicle's registration number: ")
    
    # Your API key (replace with the actual API key)
    api_key = "YOUR_API_GOES_HERE"
    
    # Query the DVLA database
    query_dvla(registration_number, api_key)
