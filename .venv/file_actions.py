import os
import shutil
def make_dir():
    mk_dir = input('Введите название папки для его создания в рабочей директории: ')
    if not os.path.isdir(mk_dir):
        os.mkdir(mk_dir)
        print(f'Создана новая папка в рабочей директории с именем {mk_dir}')
    else:
        print('Такая папка уже есть')

def delete_dir():
    del_dir = input('Введите название папки для его удаления: ')
    if os.path.isdir(del_dir):
        os.rmdir(del_dir)
        print(f'Папка {del_dir} из рабочей директории удалена')
    else:
        print('Такой папки в директории нет')

def copy_dir():
    one = input('Введите имя файла/папки для его копирования: ')
    two = input('Введите новое имя файла/папки для копирования: ')
    shutil.copy(one, two)

def see_dir():
    print(os.listdir())

def see_folders():
    for folder in os.listdir():
        if not os.path.isfile(folder):
            print(folder)

def see_files():
    for file in os.listdir():
        if os.path.isfile(file):
            print(file)

def os_info():
    print(os.name)

def creator():
    print('Создатель проги Свечников А.К.')

def replace_dir():
    replacable_dir = input('Введите директорию для дальнейшего использования в качестве рабочей: ')
    os.chdir(replacable_dir)
    print(f'Новый путь рабочей папки: {replacable_dir}')