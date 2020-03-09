# Theory 1: Adding a positive and a negative number returns a positive number if the positive number was greater


def add(x, y):
    return x + y


def test_adding_positive_negative_numbers():
    x = 1000
    y = -200
    numb = add(x, y)
    assert numb == 800

# Theory2: Adding two negative numbers returns a negative number


def test_adding_two_negative_numbers():
    numb = add(-12, -20)
    assert numb == -32

# Theory 3: Adding zero to any whole number returns that whole number


def test_adding_zero_to_whole_numbers():
    x = 0
    y = -200
    numb = add(x, y)
    assert numb == -200


