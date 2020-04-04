# Coin Challenge


def test_sum_pennies():
    user_input = '15'
    numb_of_pennies = int(user_input)
    assert numb_of_pennies == 15


def test_sum_nickels():
    user_input = '20'
    numb_of_nickels = int(user_input)
    assert numb_of_nickels == 20


def test_sum_dimes():
    user_input = '40'
    numb_of_dimes = int(user_input)
    assert numb_of_dimes == 40


def test_sum_quarters():
    user_input = '25'
    numb_of_quarters = int(user_input)
    assert numb_of_quarters == 25


def test_sum_all_coins():
    user_input = '100'
    numb_of_coins = int(user_input)
    assert numb_of_coins == 100


def test_total_under_dollar():
    user_input = '15'
    value_under = int(user_input)
    assert value_under == 15


def test_total_over_dollar():
    user_input = '22'
    excess_value = int(user_input)
    assert excess_value == 22
