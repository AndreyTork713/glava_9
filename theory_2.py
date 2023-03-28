
def main():
    phonebook = {'Крис': '555-1111', 'Кэти': '555-2222', 'Джоанна': '555-3333'}
    print(phonebook)
    print()

    phonebook.clear()
    print(phonebook)

    phonebook = {'Крис': '555-1111', 'Кэти': '555-2222', 'Джоанна': '555-3333'}
    value = phonebook.get('Эдди', 'Запись не найдена')
    print(value)
    print()
    print(phonebook.items())
    print()
    for key, value in phonebook.items():
        print(key, value)


if __name__ == '__main__':
    main()
