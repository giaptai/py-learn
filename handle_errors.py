# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero")


# print("Give 2 number and i'll divide them")

# print("Enter 'q' to quit")

while True:
    first_num = input("Enter first number: ")
    if first_num == 'q':
        break
    second_num = input("Enter first number: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) / int(second_num)
        print(answer)
    except ZeroDivisionError:
        print("You can't divide by zero")
    except ValueError:
        print("Use number only")

