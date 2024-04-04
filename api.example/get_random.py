import requests

url = "https://api.quotable.io"


response = requests.get(url + "/random")


print(response) # this will print <Response [200]>
print(response.text) # this will print the content ---> {"_id":"oQnbzQ_W0gJS","content":"Never mistake motion for action.","author":"Ernest Hemingway","tags":["Famous Quotes"],"authorSlug":"ernest-hemingway","length":32,"dateAdded":"2021-03-28","dateModified":"2023-04-14"}
print(response.json()) # This will print as dictionary ---> {'_id': 'sXDz-2N4-nnJ', 'content': 'An invasion of armies can be resisted, but not an idea whose time has come.', 'author': 'Victor Hugo', 'tags': ['Famous Quotes'], 'authorSlug': 'victor-hugo', 'length': 75, 'dateAdded': '2020-02-22', 'dateModified': '2023-04-14'}


# The below is printing only what I want in the dict --->If you want your life to be more rewarding, you have to change the way you think ----- Oprah Winfrey
response_dict = response.json()
print(response_dict["content"])
print(response_dict["author"])

