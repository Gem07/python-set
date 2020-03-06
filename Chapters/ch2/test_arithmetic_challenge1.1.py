# Adding two negative numbers returns a negative number


def add(x, y):
    return x + y


def test_adding_two_negative_numbers():
    numb = add(-2, -2)
    assert numb == -4

#
# num1 = -1
# num2 = 5
# number = add(num1, num2)
#
# if num1 < 0 and num2 < 0:
#     print(f'The output, {number} is negative')
# else:
#     print(f'The output, {number} is positive.')


