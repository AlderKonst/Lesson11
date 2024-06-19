# Простые проверки грязных функций
from file_actions import creator

def test_make_dir_isdir():
    assert make_dir() == True, 'Такой директории нет'

def test_delete_isdir():
    assert delete_dir() == False, 'Директория не удалилась'

def test_copy_dir():
    assert copy_dir() == True, 'Директория/файл не скопировался'

def test_see_dir():
    assert see_dir() == True, 'Файл listdir.txt в рабочей директории не создан'

def test_see_folders():
    folders = see_folders()
    assert len(folders) > 0, 'Не найдено ни одной папки'

def test_see_files():
    files = see_files()
    assert len(files()) > 0, 'Не найдено ни одного файла'

def test_os_info():
    name_os = os_info()
    assert name_os != '', 'Не удалось получить информацию о системе'

def test_creator_print():
    assert creator() == 'Создатель проги Свечников А.К.'

def test_replace_dir():
    assert replace_dir() == True, 'Эта директория не существует'