# Ещё раз применяю никакой декоратор, почти скопировал с предыдущего
def decorator_print():
    def decorator(f):
        def zvezda(*args, **kwargs):
            result = f(*args, **kwargs)
            print(10 * '*')
            return result
        return zvezda
    return decorator

def bank():
    import os
    import json
    @decorator_print()
    def menu():
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

    @decorator_print()
    def pays(money, history):
        try:
            # Тут тернарный оператор почти не сократит код, но усложит, не буду тут применять
            pay = int(input('Сумма покупки: '))
            if pay < money:
                name = input('Название покупки:  ')
                money -= pay
                history[name] = pay
            else:
                print('Денег не хватает!')
            with open('history.txt', 'w') as h:  # Всё таки без json не придумал как
                json.dump(history, h)
            return history
        except ValueError: # Ну, хотя бы такая обработка ...
            print("Ошибка: введенные данные не являются числом.")
            return history

    @decorator_print()
    def history_read():
        if os.path.isfile('history.txt'):
            with open('history.txt', 'r') as h: # json.load для чтения уже здесь
                history = json.load(h)
        else: history = {}
        return history

    @decorator_print()
    def histories(history):
        print('История покупок:')
        # Вот такая вод однострочка
        print(*(f'{i} за {k} рублей' for i, k in history.items()))

    @decorator_print()
    def money_write(money): # Для пополнения текущего счёта, что в файле
        money += int(input('Сумма пополнения: '))
        with open('moneys.txt', 'w') as m:
            m.write(str(money))
        return money

    @decorator_print()
    def money_read(): # Для вывода суммы текущего счёта, что в файле (при его существовании)
        if os.path.isfile('moneys.txt'):
            with open('moneys.txt', 'r') as m:
                money = int(m.read())
                print(f'На счету сейчас {money} рублей')
        else: money = 0
        return money

    @decorator_print()
    def function():
        money = money_read()
        history = history_read()

        while True:
            menu()
            choice = input('Выберите пункт меню: ')
            if choice == '1':
                money = money_write(money)

            elif choice == '2':
                history = pays(money, history)

            elif choice == '3':
                histories(history)

            elif choice == '4':
                print('Работа проги завершено')
                break
            else:
                print('Неверный пункт меню')
        return money
    function()