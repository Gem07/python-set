# Adding a positive and a negative number returns a positive number if the positive number was greater


def add(x, y):
    return x + y


def test_adding_positive_negative_numbers():
    x = 100
    y = -200
    numb = add(x, y)
    assert numb == -100


