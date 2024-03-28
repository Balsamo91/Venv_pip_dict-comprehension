# Before

user_input = input("Enter you name: ")

if user_input:
    name = user_input
else:
    name = "guest"
    
print(f"Hello, {name}")

# Cannot be shorthen as I have more input to perform like break
user_input = input("Enter you name: ")

while True:
    if user_input:
        name = user_input
        break
    else:
        print("You shall not pass!")
        
    print(f"Hello, {name}")


#  After
user_input = input("Enter you name: ")
name = user_input if user_input else "Guest"
print(f"Hello, {name}")