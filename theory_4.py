
# МНОЖЕСТВА
def main():

    myset1 = set(['один', 'два', 'три'])
    print(myset1)
    print(len(myset1))

    myset2 = set('один два три')
    print(myset2)
    print(len(myset2))

    myset3 = set(['один два три'])
    print(myset3)
    print(len(myset3))

    myset4 = set()
    myset4.add(11)
    myset4.add(21)
    myset4.add(31)
    print(myset4)

    myset4.update([41, 51, 61])
    print(myset4)
    myset4.update(myset1)
    print(myset4)
    print()
    print()

    print(myset4)
    myset4.remove(41)
    print(myset4)
    print()

    # myset4.remove(101)
    # print(myset4)

    print(myset4)
    myset4.discard(51)
    print(myset4)

    myset4.discard(101)
    print(myset4)
    print()

    print(myset4)
    print()
    print()
    print()

    # Применение цикла for для множества

    myset11 = set(['a', 'b', 'c'])
    for item in myset11:
        print(item)
    print()
    print()

    # Применение in и not in для проверки на принадлежность множеству
    myset10 = set(['a', 'b', 'c', 'd', 'e'])
    myset12 = set(['a', 'b', 'c', 'd'])
    for item in myset10:
        if item in myset12:
            print(f'Элемент {item} ВХОДИТ в множество myset12')
        elif item not in myset12:
            print(f'Элемент {item} НЕ входит в множество myset12' )

    print()
    print()
    print()

    # Объединение множеств
    print('Объединение множеств')
    print(myset1)
    print(myset11)
    myset1_11 = myset1.union(myset11)
    print(myset1_11)
    print()
    myset1234 = myset1 | myset4
    print(myset1234)
    print()
    print()

    # Пересечение множеств
    set111 = set([1, 2, 3, 4, 5, 6])
    print(set111)
    set222 = set([2, 4, 6, 8])
    print(set222)
    set333 = set111 & set222
    print(set333)


if __name__ == '__main__':
    main()