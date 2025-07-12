names = ["Long", "John", "Mary", "Alice", "Bob"]

print(names) # Print the entire list
print(names[1]) # Accessing the second element
print(names[-1])
names[1] = "Jane" # Change the second element
print(names) # Print the modified list
print(type(names)) # Check the type of the list
print(names[0:3]) # Slicing the first three elements
names.append("Ava")
print(names) # Print the list after appending a new name

names.pop(1) # Remove the second element
print(names) # Print the list after removing an element

names = ["0" for _ in range(10)] # list comprehension
print(names)