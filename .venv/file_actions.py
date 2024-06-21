import os
import shutil
def make_dir():
    mk_dir = input('Введите название папки для его создания в рабочей директории: ')
    if not os.path.isdir(mk_dir):
        os.mkdir(mk_dir)
        print(f'Создана новая папка в рабочей директории с именем {mk_dir}')
    else:
        print('Такая папка уже есть')
    return os.path.isdir(mk_dir) # Добавил для теста грязной функции

def delete_dir():
    del_dir = input('Введите название папки для его удаления: ')
    if os.path.isdir(del_dir):
        os.rmdir(del_dir)
        print(f'Папка {del_dir} из рабочей директории удалена')
    else:
        print('Такой папки в директории нет')
    return os.path.isdir(del_dir) # Добавил для теста грязной функции

def copy_dir():
    one = input('Введите имя файла/папки для его копирования: ')
    two = input('Введите новое имя файла/папки для копирования: ')
    shutil.copy(one, two)
    return os.path.exists(two) # Опять добавил для примитвного теста

def see_dir():
    files = 'files: '
    folders = 'dirs: '
    dirs = os.listdir()
    print(dirs)
    add_dir = input('Cохранить содержимое рабочей директории в файл?\ny/n\n')
    with (open('listdir.txt', 'w') as l):
        l.write(files)
        for i in dirs:
            if os.path.isfile(i):
                l.write(i)
                l.write(', ')
        l.write(f'\n{folders}')
        for i in dirs:
            if not os.path.isfile(i):
                l.write(i)
                l.write(', ')
    print('Итоговый файл с директорией создан')
    return os.path.exists('listdir.txt')  # Ещё вот добавил для примитвного теста

def see_folders():
    folders = [] # Код для теста
    for i in os.listdir():
        if not os.path.isfile(i):
            print(i)
            folders.append(i) # Код для теста
    return folders # Код для теста


def see_files():
    files = []  # Код для теста
    for i in os.listdir():
        if os.path.isfile(i):
            print(i)
            files.append(i)  # Код для теста
    return files  # Код для теста

def os_info():
    print(os.name)
    n = os.name  # Код для теста
    return n  # Код для теста

def creator():
    author = 'Создатель проги Свечников А.К.'
    print(author)
    return author

def replace_dir():
    replacable_dir = input('Введите директорию для дальнейшего использования в качестве рабочей: ')
    os.chdir(replacable_dir)
    print(f'Новый путь рабочей папки: {replacable_dir}')
    return os.path.exists(replacable_dir)  # Ещё примитвный код для теста