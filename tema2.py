'''
Radicalul unui numar dat folosind metoda lui Newton cu x0=2 si afiseaza aproximarea obtinuta
'''


def get_newton_sqrt(value, steps):
    a = value  # number to get square root of
    x0 = 2;
    for i in range(steps):
        # x_(n+1) = 0.5 * (x_n +a / x_n)

        if i != 0:
            value = (value + a / value) * 0.5
        else:
            value = (x0 + a / x0) * 0.5

    return float(value)


def test_get_newton_sqrt():
    assert get_newton_sqrt(4,2)==2.0

test_get_newton_sqrt()

'''
Afiseaza toti anii bisecti intre doi ani dati(inclsiv anii dati)
'''


def get_leap_years(start_year, year_end):
    all_leap_years =[]
    print("Anii:")
    for values in range(start_year, year_end+1):
        if check_leap_year(values):
            all_leap_years.append(values)
    return all_leap_years


'''
This function return true if year is leap/false if year is not leap
'''


def check_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def test_get_leap_years():
    assert get_leap_years(2000, 2020) == [2000, 2004, 2008, 2012, 2016, 2020]

    test_get_leap_years()


def meniu():
    '''
    Acesta este meniul principal care comunica cu utilizatorul
    :return:
    '''
    while True:
        print('''1. Execută un număr dat de pași pentru a calcula radicalul unui număr dat folosind metoda lui Newton cu x0=2 și afișează aproximarea obținută.
2. Afișează toți anii bisecți între doi ani dați (inclusiv anii dați).
3. Exit''')
        n = input('Alegeți opțiunea: ')
        if n == '1':
            valoarea = float(input('Valoarea radicalului: '))
            nr_pasi = int(input('Numarul de pasi: '))
            print(f'Raspunsul este:{get_newton_sqrt(valoarea, nr_pasi)}')
        elif n == '2':
            start_year = int(input('Anul de la care se porneste: '))
            stop_year = int(input('Anul la care ne oprim: '))
            print(f'Anii sunt: {get_leap_years(start_year, stop_year)}')
        elif n == '3':
            break
        else:print('Te rog sa introduci o valoare corecta')


meniu()