def bank():
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

    def histories(history):
        print('История покупок:')
        for i, k in history.items():
            print(f'{i} за {k} рублей')

    def function():
        money = 0
        history = {}
        while True:
            menu()
            choice = input('Выберите пункт меню: ')
            if choice == '1':
                money += int(input('Сумма пополнения: '))

            elif choice == '2':
                pays(money, history)

            elif choice == '3':
                histories(history)

            elif choice == '4':
                print('Работа проги завершено')
                break
            else:
                print('Неверный пункт меню')
    function()