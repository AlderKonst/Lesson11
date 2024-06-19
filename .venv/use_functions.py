def bank():
    import os
    import json
    def menu():
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

    def pays(money, history):
        pay = int(input('Сумма покупки: '))
        if pay < money:
            name = input('Название покупки:  ')
            money -= pay
            history[name] = pay
        else:
            print('Денег не хватает!')
        with open('history.txt', 'w') as h: # Всё таки без json не придумал как
            json.dump(history, h)
        return history

    def history_read():
        if os.path.isfile('history.txt'):
            with open('history.txt', 'r') as h: # json.load для чтения уже здесь
                history = json.load(h)
        else: history = {}
        return history

    def histories(history):
        print('История покупок:')
        for i, k in history.items():
            print(f'{i} за {k} рублей')

    def money_write(money): # Для пополнения текущего счёта, что в файле
        money += int(input('Сумма пополнения: '))
        with open('moneys.txt', 'w') as m:
            m.write(str(money))
        return money

    def money_read(): # Для вывода суммы текущего счёта, что в файле (при его существовании)
        if os.path.isfile('moneys.txt'):
            with open('moneys.txt', 'r') as m:
                money = int(m.read())
                print(f'На счету сейчас {money} рублей')
        else: money = 0
        return money


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