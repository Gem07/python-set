# Challenge 1:


def add(penny, nickel, dime, quarter):
	N = penny + nickel + dime + quarter
	return N


def multiply(value_of_coin, number_of_coins):
	total_coin_value = value_of_coin * number_of_coins
	return total_coin_value

# Three possible outcomes
# Outcome 1: player has exact number of coins


def test_player_has_exact_number():
	value_of_coin = 20
	number_of_coins = 5
	total_coin_value = multiply(value_of_coin, number_of_coins)
	assert total_coin_value == 100
	print(f'\n You won!!!🎉 You have exactly $1 😃')

# Outcome 2: Player has more than enough number of coins


def test_player_has_more_number_of_coins():
	value_of_coin = 10
	number_of_coins = 15
	total_coin_value = multiply(value_of_coin, number_of_coins)
	assert total_coin_value == 150

	over = total_coin_value - 100
	if total_coin_value > 100:
		print(f'\n Sorry player, you have more than 100. You have {over}c more!')

# Outcome 3: Player has less than enough number of coins


def test_player_has_less_number_of_coins():
	value_of_coin = 10
	number_of_coins = 9
	total_coin_value = multiply(value_of_coin, number_of_coins)
	assert total_coin_value == 90

	under = total_coin_value - 100
	if total_coin_value < 100:
		print(f'\n Sorry player, you have less than 100. You have {under}c less! 🙁')