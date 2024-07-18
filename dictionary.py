
friends_dict = {}

friends_dict = {
    'Aditya': '1234567890',
    'samarth': '1234567890',
    'kalyani': '1234567890',
    'sanket': '1234567890',
    'pranay': '1234567890'
}


print("Sorted Friends Dictionary:")
for name in sorted(friends_dict):
    print(f"{name}: {friends_dict[name]}")


search_name = input("\nEnter a name to check if it is present in the dictionary: ")


if search_name in friends_dict:
    print(f"{search_name} found in the dictionary. Phone number: {friends_dict[search_name]}")
else:
    
    phone_number = input(f"{search_name} not found. Enter phone number for {search_name}: ")
    friends_dict[search_name] = phone_number
    print(f"Added {search_name} with phone number {phone_number} to the dictionary.")


print("\nUpdated Sorted Friends Dictionary:")
for name in sorted(friends_dict):
    print(f"{name}: {friends_dict[name]}")
