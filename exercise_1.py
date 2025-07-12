age = input("Enter your age: ")
age_check = int(age)
if age_check >= 18 and age_check <= 45:
    print("Enjoy the ride!")
elif age_check < 18:
    print("You are too young to ride.")
else:
    print("You are too old to ride.")


print(3 * "hello")