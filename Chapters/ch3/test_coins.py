
def test_sum_pennies():
    user_input = '20'
    total_value_of_pennies = int(user_input) * 1
    assert total_value_of_pennies == 20


def test_sum_nickels():
    user_input = '9'
    total_value_of_nickels = int(user_input) * 5
    assert total_value_of_nickels == 45


def test_sum_dimes():
    user_input = '1'
    total_value_of_dimes = int(user_input) * 10
    assert total_value_of_dimes == 10


def test_sum_quarters():
    user_input = '1'
    total_value_of_quarters = int(user_input) * 25
    assert total_value_of_quarters == 25


def test_total_value():
    input_sum_of_coins = '100'
    if int(input_sum_of_coins) == 100:
        assert int(input_sum_of_coins) == 100


def test_total_value_over():
    input_sum_of_coins = '120'
    if int(input_sum_of_coins) > 100:
        value_over = int(input_sum_of_coins) - 100
        assert value_over == 20


def test_total_value_under():
    input_sum_of_coins = '87'
    if int(input_sum_of_coins) < 100:
        value_under = 100 - int(input_sum_of_coins)
        assert value_under == 13


