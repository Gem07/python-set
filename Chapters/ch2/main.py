# Challenge 2: Negative test


def challenge2():

    season_of_the_year = input('Enter a season of the year: ')
    if season_of_the_year == 'winter':
        print('snow')
    elif season_of_the_year == 'spring':
        print('flowers')
    elif season_of_the_year == 'summer':
        print('beach')
    elif season_of_the_year == 'fall' or season_of_the_year == 'autumn':
        print('leaves')
    else:
        print('Invalid Season!')


if __name__ == '__main__':
    challenge2()

