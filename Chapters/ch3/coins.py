
def sum_pennies(user_input):
    pennies = int(user_input) 
    return pennies


def sum_nickels(user_input):
    nickels = int(user_input)
    return nickels


def sum_dimes(user_input):
    dimes = int(user_input)
    return dimes


def sum_quarters(user_input):
    quarters = int(user_input)
    return quarters


def sum_all_coins(user_input):
    total = int(user_input)
    return total


def sum_coins_over(user_input):
    total = int(user_input)
    return total


def sum_coins_under(user_input):
    total = int(user_input)
    return total


def test_sum_pennies():
    total = sum_pennies(user_input='20')
    assert total == 20


def test_sum_nickels():
    total = sum_nickels(user_input='45')
    assert total == 45


def test_sum_dimes():
    total = sum_dimes(user_input='10')
    assert total == 10


def test_sum_quarters():
    total = sum_quarters(user_input='25')
    assert total == 25


def test_sum_all_coins():
    exactly_100_cents = sum_all_coins(user_input='100')
    if int(sum_all_coins(user_input='100')) == 100:
        assert exactly_100_cents == 100
        print(f'\nYou have won! You have exactly 100¢ or $1!!!')


def test_sum_coins_over():
    over_100_cents = sum_coins_over(user_input='122')
    if int(sum_coins_over(user_input='122')) > 100:
        amount_over = over_100_cents - 100
        assert amount_over == 22
        print(f'\n Sorry, you have exceeded $1 by 22¢')


def test_sum_coins_under():
    under_100_cents = sum_coins_under(user_input='89')
    if int(sum_coins_under(user_input='89')) < 100:
        amount_under = 100 - under_100_cents
        assert  amount_under == 11
        print(f'\n Sorry, you are under $1 by 11¢')


# def test_total_value():
#     input_sum_of_coins = '100'
#     if int(input_sum_of_coins) == 100:
#         assert int(input_sum_of_coins) == 100
#
# def test_total_value_over():
#     input_sum_of_coins = '120'
#     if int(input_sum_of_coins) > 100:
#         value_over = int(input_sum_of_coins) - 100
#         assert value_over == 20
#
#
# def test_total_value_under():
#     input_sum_of_coins = '87'
#     if int(input_sum_of_coins) < 100:
#         value_under = 100 - int(input_sum_of_coins)
#         assert value_under == 13
#
#
