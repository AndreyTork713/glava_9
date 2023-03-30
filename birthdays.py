# Эта программа применяет словарь для хранения
# имен и дней рождения друзей.

# ГЛОБАЛЬНЫЕ КОНСТАНТЫ

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


# Главная функция
def main():
    # Создать пустой словарь
    birthdays = {}

    # Инициализировать переменную для выбора пользователя
    choice = 0

    while choice != QUIT:

        # Получить выбранный пользователем пункт меню
        choice = get_menu_choice()
        # Обработать выбор пользователя:
        if choice == LOOK_UP:
            look_app(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)


# функция выводит меню и получает проверенный
# на допустимость выбранный пользователем пункт.
def get_menu_choice():
    print()
    print('Друзья и их дни рождения')
    print('------------------------')
    print('1. Найти день рождения.')
    print('2. Добавить новый день рождения.')
    print('3. Изменить день рождения.')
    print('4. Удалить день рождения.')
    print('5. Выйти из программы.')
    print()

    # Получить выбранный пункт меню.
    choice = int(input('Введите выбранный пункт: '))

    return choice


def look_app(birthdays):
    pass

def add(birthdays):
    pass

def change(birthdays):
    pass

def delete(birthdays):
    pass
