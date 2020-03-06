# Adding a positive and a negative number returns a positive number if the positive number was greater


def add(x, y):
    return x + y


def test_adding_positive_negative_numbers():
    x = 100
    y = -200
    numb = add(x, y)
    assert numb == -100
    # if x > y:
    #     print(f'\n \n The output, {numb} is positive.')
    # else:
    #     print(f'\n\n The output is {numb} is negative.')

# num1 = 3
# num2 = -2
# number = add(num1, num2)

# if num1 > num2:
#     print(f'The output, {number} is positive.')

