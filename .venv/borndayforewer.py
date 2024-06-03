def victorina():
    def year_day():
        year = input('Ввведите год рождения А.С.Пушкина:')
        while year != '1799':
            print("Не верно")
            year = input('Ввведите год рождения А.С.Пушкина:')
        day()
    def day():
        day = input('Ввведите день рождения Пушкин?')
        while day != '6':
            print("Не верно")
            day = input('В какой день июня родился Пушкин?')
        print('Верно')
    year_day()