# Вот такой вот простейший декоратор
def decorator_print():
    def decorator(f):
        def wrapper(*args, **kwargs):
            result = f(*args, **kwargs)
            print("Викторина успешно завершена!")
            return result
        return wrapper
    return decorator

@decorator_print()
def victorina():
    def year_day():
        while True:
            try:
                year = int(input('Ввведите год рождения А.С.Пушкина:'))
                if year == 1799:
                    print("Верно")
                    break
                print("Не верно")
            except ValueError:
                print("Вы должны ввести число")
        day()

    def day():
        while True:
            try:
                day = int(input('Вввените день рождения Пушкин?'))
                if day == 6:
                    print('Верно')
                    break
                print("Не верно")
            except ValueError:
                print("Вы должны ввести число")
    year_day()