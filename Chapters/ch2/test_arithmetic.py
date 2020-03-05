# test

def add(x, y):
    return x + y


def test_adding_even_numbers():
    number = add(2, 2)
    assert number == 4



#Questions
# 1) do i define all the functions I create "if __name__ == '__main__':
#     add()
#     test_adding_positive_negative_numbers()
#     test_adding_two_negative_numbers()
#     test_adding_zero()
# Otherwise, which do i actually need? - don't include them in your main() function
#
# 2) how many test_ files can i have within a package?
