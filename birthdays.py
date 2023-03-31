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
    # Получить имя:
    name = input('Введите имя: ')
    # Отыскать имя в словаре
    print(birthdays.get(name, 'Имя не найдено.'))


def add(birthdays):
    # Получит имя и день рождения
    name = input('Введите имя: ')
    bday = input('Введите день рождения: ')

    if name not in birthdays:
        birthdays[name] = bday
        print('Запись добавлена')
    else:
        print('Эта запись уже существует')


def change(birthdays):
    name = input('Введите имя: ')
    if name in birthdays:
        # Получит новый день рождения:
        bday = input('Введите новый день рождения: ')
        # Обновить запись
        birthdays[name] = bday
    else:
        print('Это имя не найдено.')


def delete(birthdays):
    name = input('Введите имя: ')

    if name in birthdays:
        del birthdays[name]
    else:
        print('Имя не найдено')


if __name__ == '__main__':
    main()

