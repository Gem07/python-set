
# Adding zero to any whole number returns that whole number


def add(x, y):
    return x + y


def test_adding_zero_to_whole_numbers():
    x = 0
    y = -200
    numb = add(x, y)
    assert numb == -200


# num1 = 0
# num2 = 18
# number = add(num1, num2)
#
# if num1 > 0 or num2 > 0:
#     print(f'The sum {number} is always equal to the whole number.')
