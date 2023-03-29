
def main():
    phonebook = {'Крис': '555-1111', 'Кэти': '555-2222', 'Джоанна': '555-3333'}
    print(phonebook)
    print()

    # метод clear()
    phonebook.clear()
    print(phonebook)

    # метод get()
    phonebook = {'Крис': '555-1111', 'Кэти': '555-2222', 'Джоанна': '555-3333'}
    value = phonebook.get('Эдди', 'Запись не найдена')
    print(value)
    print()

    # метод items()
    print(phonebook.items())
    print()
    for key, value in phonebook.items():
        print(key, value)

    # метод keys()
    phonebook = {'Крис': '555-1111', 'Кэти': '555-2222', 'Джоанна': '555-3333'}
    for key in phonebook.keys():
        print(key)
    print()

    # метод pop(). Возвращает связанное с ключем значение и удаляет эту пару из словаря
    phonebook = {'Крис': '555-1111', 'Кэти': '555-2222', 'Джоанна': '555-3333'}
    print(phonebook)
    phone_number = phonebook.pop('Крис', 'Значение не найдено')
    print(phone_number)
    print(phonebook)
    print()

    # метод popitem() Удаляет случайную пару из словаря и возвращает её в качестве кортежа(?!)
    phonebook = {'Крис': '555-1111', 'Кэти': '555-2222', 'Джоанна': '555-3333'}
    print(phonebook)
    key, value = phonebook.popitem()
    print(key, value)
    print(phonebook)
    print()

    # метод values()
    phonebook = {'Крис': '555-1111', 'Кэти': '555-2222', 'Джоанна': '555-3333'}
    for value in phonebook.values():
        print(value)
    print(phonebook.values())
    print()


if __name__ == '__main__':
    main()
