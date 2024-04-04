import requests

# https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=precipitation_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}`

# latitude = bbb

url = "https://api.open-meteo.com/v1/forecast?latitude=53.40311&longitude=-6.27021&daily=precipitation_sum&timezone=Europe%2FLondon&start_date=2024-04-05&end_date=2024-04-05"


# 53.40311/-6.27021 ---> Dublin Coordinates

respone = requests.get(url)

print(respone.text)