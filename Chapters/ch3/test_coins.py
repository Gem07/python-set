print("~~~~~Coin Challenge~~~~~")


def test_sum_pennies():
    user_input = '15'
    value_of_pennies = int(user_input) * 1
#   sum_of_coins = numb_of_pennies * 1
    assert value_of_pennies == 15
#   assert sum_of_coins ==


def test_sum_nickels():
    user_input = '4'
    value_of_nickels = int(user_input) * 5
    assert value_of_nickels == 20


def test_sum_dimes():
    user_input = '4'
    value_of_dimes = int(user_input) * 10
    assert value_of_dimes == 40


def test_sum_quarters():
    user_input = '1'
    value_of_quarters = int(user_input) * 25
    assert value_of_quarters == 25


def test_sum_all_coins():
    user_input = '100'
    total_number_of_coins = int(user_input)
    assert total_number_of_coins == 100


def test_total_under_dollar():
    user_input = '85'
    value_under = 100 - int(user_input)
    assert value_under == 15


def test_total_over_dollar():
    user_input = '107'
    excess_amount = int(user_input) - 100
    assert excess_amount == 7
