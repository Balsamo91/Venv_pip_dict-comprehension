# IT WORKS SO IF ISSUES PASTE BACK THIS IN TXT FILE"
'''
{"latitude": 53.4, "longitude": -6.27, "generationtime_ms": 0.02193450927734375, "utc_offset_seconds": 3600, "timezone": "Europe/London", "timezone_abbreviation": "BST", "elevation": 67.0, "daily_units": {"time": "iso8601", "precipitation_sum": "mm"}, "daily": {"time": ["2024-04-06"], "precipitation_sum": [-1.5]}}
{"latitude": 53.4, "longitude": -6.27, "generationtime_ms": 0.02193450927734375, "utc_offset_seconds": 3600, "timezone": "Europe/London", "timezone_abbreviation": "BST", "elevation": 67.0, "daily_units": {"time": "iso8601", "precipitation_sum": "mm"}, "daily": {"time": ["2024-04-07"], "precipitation_sum": [4.5]}}
{"latitude": 53.4, "longitude": -6.27, "generationtime_ms": 0.01800060272216797, "utc_offset_seconds": 3600, "timezone": "Europe/London", "timezone_abbreviation": "BST", "elevation": 67.0, "daily_units": {"time": "iso8601", "precipitation_sum": "mm"}, "daily": {"time": ["2024-04-08"], "precipitation_sum": [20.3]}}

'''

'''
#  import requests
#  import datetime

# Ask user for a date, if empty take current dates

#  check if data is inside a file, if it is: print data from file and quit the program

# if data not in file:
    # structure the url, pass necesseray details

    # make a get requests to the API

    # Parse response to dict for easy access

# Check the precipitation_sum value:
# if bigger than 0 print(it will rain and a mm value)
# if equals to 0: it will not rain
# else print I do not know

# save data into file - date and precipitation_sum
'''



print("\nWelcome to Valerio's Forecast!")

import datetime
import requests
# # import geocoder
import json

url = "https://api.open-meteo.com"

while True:
    searched_date = input("\nPlease enter the date in the following format yyyy-mm-dd, if empty the current date will be used: ")
    
    if searched_date.strip() == "":
        # Get the current date and time
        current_time = datetime.datetime.now()
        # Extract year, month, and day
        year = current_time.year
        month = current_time.month
        day = current_time.day

        searched_date = f"{year}-{month:02d}-{day:02d}"

    found = False
    with open("dates.txt", "r+") as file:
        for line in file:
            dictionary = json.loads(line)
            daily = dictionary.get("daily", {})
            time = daily.get("time", [])

            if searched_date in time:
                found = True
                precip_value = daily.get("precipitation_sum", [])
                print(precip_value)
                for v in precip_value:

                    if v > 0.0:
                        print(f"It will rain as precipitation value is: {v}")
                        break
                        
                    elif v == 0.0:
                        print(f"It will not rain as precipitation value is: {v}")
                        break

                    else:
                        print("I do not Know!")
                        break
    
        if not found:
                
            # latitude = input("\nPlease enter latitude: ")
            # longitude = input("\nPlease enter longitude: ")
            response = requests.get(url + f"/v1/forecast?latitude=53.40311&longitude=-6.27021&daily=precipitation_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}")

            response_json = response.json()
            response_write = json.dumps(response_json) + '\n'
            file.write(response_write)

            daily_precip_sum = response_json.get("daily", {})
            precipitation_sum = daily_precip_sum.get("precipitation_sum", [])
            # print("Precipitation Sum: ")
            for value in precipitation_sum:
                if value > 0.0:
                    print(f"It will rain as precipitation value is: {value}")
                    break

                elif value == 0.0:
                    print(f"It will not rain as precipitation value is: {value}")
                    break

                else:
                    print("I do not Know!")
                    break

    if input("Would you like to continue? (yes/no): ").lower() != "yes":
        file.close() # Close the file before exiting the loop
        break





