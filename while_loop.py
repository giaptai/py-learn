count = 1 
while count <= 200:
    print("Count is:", count)

    user_input = input("Enter 'exit' to stop ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    count+=1