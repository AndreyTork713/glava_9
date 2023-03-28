def main():
    phonebook = {'Крис': '555-1111', 'Кэти': '555-2222', 'Джоанна': '555-3333'}
    print(phonebook)
    for key in phonebook:
        print(f'номер {key}: {phonebook[key]}')
    try:
        if 'Кэти' in phonebook:
            print(f'{"Кэти"} есть в словаре')
            print(f'номер Кэти: {phonebook["Кэти"]}')

        print(phonebook['Anton'])

    except:
        print('Такого имени нет в словаре.')

    phonebook['Антон'] = '555-4444'
    print(phonebook)
    num_items = len(phonebook)
    print(num_items)
    print()

    del phonebook['Крис']
    print(phonebook)
    num_items = len(phonebook)
    print(num_items)

    test_scores = {'Кайла': [88, 92, 100],
                   'Луис': [95, 74, 81],
                   'Софи': [72, 88, 91],
                   'Итан': [70, 75, 78]
                   }
    print(test_scores)
    print(test_scores['Софи'])
    kayla_scores = test_scores['Кайла']
    print(kayla_scores)
    print()

    mixed_up = {'abc': 1, 999: 'tada-tada', (3, 6, 9): (3, 6, 9)}
    print(mixed_up)
    print()

    employee = {'фио': 'Кевин Смит', 'ID': '12345', 'ставка': 25.75}
    print(employee)


if __name__ == '__main__':
    main()
