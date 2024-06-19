def victorina():
    def year_day():
        year = input('Ввведите год рождения А.С.Пушкина:')
        while year != '1799':
            print("Не верно")
            year = input('Ввведите год рождения А.С.Пушкина:')
        day()
        assert type(year) is int, 'Нужно вводить числа целые'
    def day():
        day = input('Ввведите день рождения Пушкин?')
        while day != '6':
            print("Не верно")
            day = input('В какой день июня родился Пушкин?')
            assert type(day) is int, 'Нужно вводить числа целые'
        print('Верно')
    year_day()
