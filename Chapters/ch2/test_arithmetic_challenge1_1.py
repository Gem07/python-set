# Adding two negative numbers returns a negative number


def add(x, y):
    return x + y


def test_adding_two_negative_numbers():
    numb = add(-2, -2)
    assert numb == -4
