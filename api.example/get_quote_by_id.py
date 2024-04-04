import requests

url = "https://api.quotable.io"

# response = requests.get(url + "/quotes/_cllvgW3qw9C")

# print(response.text)



response = requests.get(url + "/quotes/_cllvgW3")
# response = requests.get(url + "/quotes/_cllvgW3qw9C")
print(response.status_code)



