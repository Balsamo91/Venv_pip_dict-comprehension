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

# g = geocoder.google(input("please provide city: "))
# ask = input
# g = geocoder.google("Dublin")
# def ask_for_date():
#     date = input("please provide a date in the 'YYYY-mm-dd' format: ")
# print(g)
##########################################
# 'daily': {'time': ['2024-04-05']
# with open("dates.txt", "r") as file:
#     for lines in file:
#         date = json.loads(lines)
#         print(type(date))
#         for i in date:
#             daily_file = i["daily"]
#             print(daily_file)

import datetime
import requests
# # import geocoder
import ast


# response = requests.get(url + f"v1/forecast?latitude={latitude}&longitude={longitude}&daily=precipitation_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}")


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


    with open("dates.txt", "r") as file:
        date = file.read()
        dictionary = ast.literal_eval(date) # Convert string to dictionary
        daily = dictionary.get("daily", {})
        time = daily.get("time", [])

        date_found = False
        for d in time:
            if searched_date == d:
                date_found = True
                break
        if date_found:
            print(dictionary)
            break
            
    if not date_found: 
        # latitude = input("\nPlease enter latitude: ")
        # longitude = input("\nPlease enter longitude: ")
        response = requests.get(url + f"/v1/forecast?latitude=53.40311&longitude=-6.27021&daily=precipitation_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}")
        
        response_json = response.json()
        # print(response)
        # print(type(response_json))
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

                                             




    








    # print(time)


# if searched_date == time:
#     print(date)

# else:
#     print("NANANANANANAN")






# file_rw = open("dates.txt", "r")
# print(file_rw.read())




# put the below in a If statement search_date is not in 'file.txt':
# latitude = input("\nPlease enter latitude: ")
# longitude = input("\nPlease enter longitude: ")


# response = requests.get(url + f"v1/forecast?latitude={latitude}&longitude={longitude}&daily=precipitation_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}")








