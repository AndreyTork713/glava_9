def main():

    # Включение в словарь
    numbers = [2, 4, 6, 8]
    print(f'numbers = {numbers}')
    squares = {item: item**2 for item in numbers}
    print(f'squares = {squares}')
    print()

    # Создание копии словаря с помощью включения в словарь
    # Метод items() возвращает все элементы словаря в виде последовательностей кортежей
    # [('k','v'),('k','v'),('k','v')]
    phonebook = {'Крис': '555-1111', 'Кэти': '555-2222', 'Джоанна': '555-3333'}
    copy_phonebook = {k: v for k, v in phonebook.items()}
    print(f'phonebook = {phonebook}')
    print(f'copy_phonebook = {copy_phonebook}')
    print()
    # Использование условия IF для выбора элементов словаря
    populations = {'Нью-Йорк': 8398748, 'Лос-Анджелес': 3990456,
                   'Чикаго': 2705994, 'Хьюстон': 2325502,
                   'Феникс': 1660272, 'Филадельфия': 1584138}
    print(f'populations = {populations}')

    # Метод items() возвращает все элементы словаря в виде последовательностей кортежей
    # [('k','v'),('k','v'),('k','v')]
    largest = {k: v for k, v in populations.items() if v > 2000000}
    print(f'largest = {largest}')


if __name__ == '__main__':
    main()