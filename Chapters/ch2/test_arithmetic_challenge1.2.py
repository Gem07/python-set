
# Adding zero to any whole number returns that whole number


def add(x, y):
    return x + y


def test_adding_zero_to_whole_numbers():
    numb = add(90, 0)
    assert numb == 90


num1 = 0
num2 = 18
number = add(num1, num2)

if num1 > 0 or num2 > 0:
    print(f'The sum {number} is always equal to the whole number.')
