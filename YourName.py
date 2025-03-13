# Define a function that responds with a personaLized greeting
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

first_name = input() # Read the first name
last_name = input() # Read the last name
print_full_name(first_name, last_name) # Call the function