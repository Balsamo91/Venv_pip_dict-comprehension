import requests

url = "https://api.quotable.io"

# _cllvgW3qw9C
quote_id = input("quote ID: ")

response = requests.get(url + f"/quotes/{quote_id}")


if response.status_code == 200:
    response_dict = response.json()
    print("\n" + response_dict["content"])
    print(response_dict["author"])

elif response.status_code > 400:
    print("\nFailed")
    print("Reason: " + response.text + "\n")

else:
    print("Failed unknown reason!")