# import geocoder

# city = input("Enter the name of the city: ").capitalize()
# location = geocoder.arcgis(city)
# print(location)

# if location.ok:
#     latitude = location.latlng[0]
#     longitude = location.latlng[1]
#     print(f"The latitude of {city} is {latitude} and the longitude is {longitude}.")
# else:
#     print("Could not find coordinates for the city.")


import geocoder

# Assuming you have latitude and longitude variables
latitude = 40.7128
longitude = -74.0060

# Perform reverse geocoding to get the city name
location = geocoder.arcgis([latitude, longitude], method='reverse')

if location.ok:
    city = location.city
    print(f"The coordinates ({latitude}, {longitude}) correspond to the city of {city}.")
else:
    print("Could not find the city corresponding to the coordinates.")
