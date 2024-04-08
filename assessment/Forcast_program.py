print("\nWelcome to Valerio's Forecast!")

import datetime
import requests
import geocoder
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
        # Combine year+month+day to have them shown in the expected format
        searched_date = f"{year}-{month:02d}-{day:02d}"

    else:
        try:
            datetime.datetime.strptime(searched_date, "%Y-%m-%d")
        except ValueError:
            print("\nInvalid date format. Make sure to use 'YYYY-MM-DD' format!")
            continue

    city = input("\nWhat city do you want to check? ").capitalize()

    found = False
    with open("dates.txt", "r+") as file:
        for line in file:
            dictionary = json.loads(line)

            # Parsing latitude and longitude in dates.txt
            latitude =dictionary["latitude"]
            longitude = dictionary["longitude"]

            # Parsing daily dict in dates.txt
            daily = dictionary.get("daily", {})
            time = daily.get("time", [])

            # Checking if the input date is matching in time variable AND the input city is matching city using the reverse method from the coordinates found in file 
            if searched_date in time and city in geocoder.arcgis([latitude, longitude], method='reverse').city:
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
            location = geocoder.arcgis(city)

            if location.ok:
                latitude = location.latlng[0]
                longitude = location.latlng[1]

                response = requests.get(url + f"/v1/forecast?latitude={latitude}&longitude={longitude}&daily=precipitation_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}")

                response_json = response.json()
                response_write = json.dumps(response_json) + '\n'
                file.write(response_write)

                daily_precip_sum = response_json.get("daily", {})
                precipitation_sum = daily_precip_sum.get("precipitation_sum", [])
                
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
            else:
                print("\nCould not find coordinates for the city.")

    if input("\nWould you like to continue? (yes/no): ").lower() != "yes":
        file.close() # Close the file before exiting the loop
        print("Bye, have a good one!")
        break
