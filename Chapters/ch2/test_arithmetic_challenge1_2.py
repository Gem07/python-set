# Adding zero to any whole number returns that whole number


def add(x, y):
    return x + y


def test_adding_zero_to_whole_numbers():
    x = 0
    y = -200
    numb = add(x, y)
    assert numb == -200

