def victorina():
    def year_day():
        year = int(input('Ввведите год рождения А.С.Пушкина:'))
        while year != '1799':
            print("Не верно")
            year = int(input('Ввведите год рождения А.С.Пушкина:'))
        day()
        assert type(year) is int, 'Нужно вводить числа целые'
    def day():
        day = int(input('Ввведите день рождения Пушкин?'))
        while day != '6':
            print("Не верно")
            day = int(input('В какой день июня родился Пушкин?'))
            assert type(day) is int, 'Нужно вводить числа целые'
        print('Верно')
    year_day()
