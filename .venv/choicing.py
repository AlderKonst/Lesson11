def thirteen():
    import os
    import file_actions as fa
    from input_menu import menu
    from borndayforewer import victorina
    from use_functions import bank
    while True:
        choice = menu()
        if choice == '1':
            fa.make_dir()
        elif choice == '2':
            fa.delete_dir()
        elif choice == '3':
            fa.copy_dir()
        elif choice == '4':
            fa.see_dir()
        elif choice == '5':
            fa.see_folders()
        elif choice == '6':
            fa.see_files()
        elif choice == '7':
            fa.os_info()
        elif choice == '8':
            fa.creator()
        elif choice == '9':
            victorina()
        elif choice == '10':
            bank()
        elif choice == '11':
            fa.replace_dir()
        elif choice == '12':
            print('Работа проги завершено!')
            break
        else:
            print('Неверный пункт меню')

        assert 0 < int(choice) < 13, 'Введено число за пределами пунктов 1 ... 12'
        assert type(int(choice)) is int, 'Введено не число'