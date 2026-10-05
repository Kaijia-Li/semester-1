# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")                    # Print the original input string
print(f"Modified String 1: {user_string.lower()}")            # Convert all letters to lowercase
print(f"Modified String 2: {user_string.upper()}")            # Convert all letters to uppercase
print(f"Modified String 3: {user_string.strip()}")            # Remove whitespace from start and end
print(f"Modified String 4: {user_string.replace('a', '@')}")  # Replace every 'a' character with '@'
print(f"Modified String 5: {user_string.capitalize()}")       # Capitalise the first character, rest lowercase
print(f"Modified String 6: {user_string[::-1]}")              # Reverse the whole string
print(f"Modified String 7: {user_string.title()}")            # Capitalise the first letter of every word
print(f"Modified String 8: {len(user_string)}")               # Return the total number of characters
print(f"Modified String 9: {user_string.find('a')}")          # Find index of first 'a', return -1 if not found
print(f"Modified String 10: {user_string.count('a')}")        # Count how many times 'a' appears
print(f"Modified String 11: {user_string.startswith('Hello')}")# Check if string starts with 'Hello', return True/False
print(f"Modified String 12: {user_string.endswith('!')}")     # Check if string ends with '!', return True/False
print(f"Modified String 13: {user_string.isalnum()}")         # Check if all characters are letters or numbers
print(f"Modified String 14: {user_string.isalpha()}")         # Check if all characters are alphabet letters
print(f"Modified String 15: {user_string.isdigit()}")         # Check if all characters are numeric digits


######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!