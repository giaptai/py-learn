def add_number(num1, num2):
    result = num1 + num2
    return result

sum_result = add_number(1, 7)

print(f'The sum is {sum_result}')


def concat_uppercase(str1, str2):
    result = str1 + str2
    return result.upper()

concattented_str = concat_uppercase("hello ", "Thu")

print(concattented_str)
