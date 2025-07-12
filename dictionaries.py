# customer = {
#     "id": 101,
#     "name": "John Doe",
#     "phone": "123-456-7890",
#     "premium_membder": True
# }

# print(customer)  # Print the entire dictionary
# print(customer["id"]) # Accessing the value of the key "id"
# print(customer["name"]) # Accessing the value of the key "name"
# print(customer["phone"]) # Accessing the value of the key "phone"
# print(customer["premium_membder"]) # Accessing the value of the key "premium_member"


customers = [
    {
        "id": 101,
        "name": "John Doe",
        "phone": "123-456-7890",
        "premium_membder": True
    },
    {
        "id": 102,
        "name": "Jane Smith",
        "phone": "987-654-3210",
        "premium_membder": False
    }
]

for customer in customers:
    print(customer.items())  # Print all key-value pairs in the dictionary
    print(customer["id"])  # Accessing the value of the key "id"
    print(customer["name"])  # Accessing the value of the key "name"
    print(customer["phone"])  # Accessing the value of the key "phone"
    print(customer["premium_membder"])  # Accessing the value of the key "premium_member"
    print("_________________________________")      